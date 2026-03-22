from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, Response, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from functools import wraps
from datetime import datetime
import os
import csv
import uuid
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bloomburrow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ── Upload config ─────────────────────────────────────────────────────────────
BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER  = os.path.join(BASE_DIR, 'static', 'uploads')
ALLOWED_EXT    = {'jpg', 'jpeg'}   # JPG only for security
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER']          = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH']     = 10 * 1024 * 1024   # 10 MB

# ── Email config (Gmail) ─────────────────────────────────────────────────────
app.config['MAIL_SERVER']        = 'smtp.gmail.com'
app.config['MAIL_PORT']          = 587
app.config['MAIL_USE_TLS']       = True
app.config['MAIL_USERNAME']      = 'bloomburrow26@gmail.com'
app.config['MAIL_PASSWORD']      = 'dnppalqmcgptmqtj'
app.config['MAIL_DEFAULT_SENDER']= 'bloomburrow26@gmail.com'

NOTIFY_EMAIL = 'bloomburrow26@gmail.com'

# ── CSV file paths ────────────────────────────────────────────────────────────
ACCOUNTS_CSV = os.path.join(BASE_DIR, 'accounts.csv')
ORDERS_CSV   = os.path.join(BASE_DIR, 'orders.csv')

db            = SQLAlchemy(app)
mail          = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view              = 'login'
login_manager.login_message           = 'Please log in to continue.'
login_manager.login_message_category  = 'info'


# ── Models ────────────────────────────────────────────────────────────────────

class User(UserMixin, db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin      = db.Column(db.Boolean, default=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)
    bookings      = db.relationship('Booking', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Booking(db.Model):
    id                 = db.Column(db.Integer, primary_key=True)
    booking_ref        = db.Column(db.String(4), unique=True, nullable=True)
    user_id            = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    package            = db.Column(db.String(20), nullable=False)
    pax                = db.Column(db.Integer, nullable=False)
    price              = db.Column(db.Integer, nullable=False)
    event_date         = db.Column(db.String(50), nullable=False)
    event_venue        = db.Column(db.String(200), nullable=False)
    phone              = db.Column(db.String(20), default='')
    notes              = db.Column(db.Text, default='')
    status             = db.Column(db.String(20), default='Pending')
    payment_status     = db.Column(db.String(30), default='Awaiting Payment')
    payment_screenshot = db.Column(db.String(300), default='')
    cost               = db.Column(db.Float, default=0.0)
    hours_spent        = db.Column(db.Float, default=0.0)
    event_start_time   = db.Column(db.String(5), default='')
    event_end_time     = db.Column(db.String(5), default='')
    created_at         = db.Column(db.DateTime, default=datetime.utcnow)
    chat_messages      = db.relationship('ChatMessage', backref='booking', lazy=True)


class ChatMessage(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    sender_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    body       = db.Column(db.Text, nullable=False)
    is_read    = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sender     = db.relationship('User', backref='chat_messages')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ── Admin decorator ───────────────────────────────────────────────────────────

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated


# ── File upload helpers ───────────────────────────────────────────────────────

def allowed_file(filename):
    """Check that the file extension is JPG/JPEG."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


def is_real_jpeg(file_storage):
    """Verify the file starts with the JPEG magic bytes (FFD8FF).
    This prevents someone renaming a non-image file to .jpg."""
    header = file_storage.stream.read(3)
    file_storage.stream.seek(0)   # rewind so Flask can still save the file
    return header == b'\xff\xd8\xff'


def generate_booking_ref():
    """Return a unique 4-digit booking reference string (e.g. '4821')."""
    while True:
        ref = str(random.randint(1000, 9999))
        if not Booking.query.filter_by(booking_ref=ref).first():
            return ref


# ── Package data ──────────────────────────────────────────────────────────────

PACKAGES = {
    '40': {
        'pax': 40,
        'price': 388,
        'original_price': 488,
        'label': '40 Pax',
        'badge': 'PROMO',
        'description': 'Perfect for intimate gatherings and small weddings.',
        'features': [
            'Fresh seasonal flowers',
            'Wrapping materials & vases',
            'Delivery, set-up & tear down',
            '2 Florists on-site',
        ],
    },
    '80': {
        'pax': 80,
        'price': 688,
        'original_price': None,
        'label': '80 Pax',
        'badge': 'POPULAR',
        'description': 'Our most popular package for medium-sized weddings.',
        'features': [
            'Fresh seasonal flowers',
            'Wrapping materials & vases',
            'Delivery, set-up & tear down',
            '2 Florists on-site',
        ],
    },
    '120': {
        'pax': 120,
        'price': 968,
        'original_price': None,
        'label': '120 Pax',
        'badge': None,
        'description': 'Our most popular package for mid-sized weddings.',
        'features': [
            'Fresh seasonal flowers',
            'Wrapping materials & vases',
            'Delivery, set-up & tear down',
            '2 Florists on-site',
        ],
    },
}


# ── CSV helpers ───────────────────────────────────────────────────────────────

def log_account_to_csv(user, plain_password=''):
    file_exists = os.path.isfile(ACCOUNTS_CSV)
    with open(ACCOUNTS_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'email', 'password', 'created_at'])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'id':         user.id,
            'name':       user.name,
            'email':      user.email,
            'password':   plain_password,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })


def log_order_to_csv(booking, user, pkg):
    file_exists = os.path.isfile(ORDERS_CSV)
    with open(ORDERS_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'booking_id', 'user_id', 'user_name', 'user_email',
            'package', 'pax', 'price',
            'event_date', 'event_venue', 'notes',
            'status', 'payment_status', 'created_at',
        ])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'booking_id':     booking.id,
            'user_id':        user.id,
            'user_name':      user.name,
            'user_email':     user.email,
            'package':        pkg['label'],
            'pax':            booking.pax,
            'price':          booking.price,
            'event_date':     booking.event_date,
            'event_venue':    booking.event_venue,
            'notes':          booking.notes or '',
            'status':         booking.status,
            'payment_status': booking.payment_status,
            'created_at':     booking.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })


# ── Email helper ──────────────────────────────────────────────────────────────

def send_booking_notification(booking, user, pkg):
    """Notify admin of a new booking."""
    try:
        time_line = f"{booking.event_start_time} – {booking.event_end_time}" if booking.event_start_time else '—'
        subject = f"🌿 New Booking — {pkg['label']} Package ({user.name})"
        body = f"""
Hi,

A new booking has been submitted on Bloom Burrow! Here are the details:

──────────────────────────────
  Booking # : {booking.booking_ref}
  Customer  : {user.name}
  Email     : {user.email}
  Phone     : +65 {booking.phone or '—'}
  Package   : {pkg['label']} ({booking.pax} pax)
  Price     : S${booking.price}
  Event Date: {booking.event_date}
  Time      : {time_line}
  Venue     : {booking.event_venue}
  Notes     : {booking.notes or '—'}
  Booked at : {booking.created_at.strftime('%d %b %Y, %I:%M %p')}
──────────────────────────────

Please log in to the admin panel to review and confirm this booking.
https://bloomburrow.sg/admin

– Bloom Burrow System
        """.strip()
        msg = Message(subject=subject, recipients=[NOTIFY_EMAIL], body=body)
        mail.send(msg)
    except Exception as e:
        app.logger.warning(f"Could not send admin notification email: {e}")


def send_booking_confirmation(booking, user, pkg):
    """Send booking confirmation email to the customer."""
    try:
        time_line = f"{booking.event_start_time} – {booking.event_end_time}" if booking.event_start_time else '—'
        subject = f"🌸 Your Bloom Burrow Booking is Received — #{booking.booking_ref}"
        body = f"""
Hi {user.name},

Thank you for booking with Bloom Burrow! We've received your request and will confirm it shortly after reviewing your payment.

──────────────────────────────
  Booking # : {booking.booking_ref}
  Package   : {pkg['label']} ({booking.pax} pax)
  Price     : S${booking.price}
  Event Date: {booking.event_date}
  Time      : {time_line}
  Venue     : {booking.event_venue}
──────────────────────────────

What happens next:
1. Complete your PayLah payment if you haven't already.
2. Upload your payment screenshot on your booking page.
3. We'll confirm your booking within 1–2 business days.

You can view your booking and chat with us anytime at:
https://bloomburrow.sg/dashboard

If you have any questions, just reply to this email.

With love,
The Bloom Burrow Team 🌸
        """.strip()
        msg = Message(subject=subject, recipients=[user.email], body=body)
        mail.send(msg)
    except Exception as e:
        app.logger.warning(f"Could not send customer confirmation email: {e}")


def send_status_update(booking, user, new_status):
    """Notify the customer when admin changes their booking status."""
    try:
        pkg_label = PACKAGES[booking.package]['label'] if booking.package in PACKAGES else f"{booking.package} Pax"
        time_line = f"{booking.event_start_time} – {booking.event_end_time}" if booking.event_start_time else '—'

        if new_status == 'Confirmed':
            subject = f"✅ Booking Confirmed — Bloom Burrow #{booking.booking_ref}"
            headline = "Great news — your booking has been confirmed!"
            extra = "Please arrive 15–20 minutes before your event start time. Our florists will be set up and ready for your guests."
        elif new_status == 'Cancelled':
            subject = f"❌ Booking Cancelled — Bloom Burrow #{booking.booking_ref}"
            headline = "Your booking has been cancelled."
            extra = "If you believe this is a mistake or would like to rebook, please get in touch with us through your booking page."
        else:
            subject = f"📋 Booking Update — Bloom Burrow #{booking.booking_ref}"
            headline = f"Your booking status has been updated to: {new_status}."
            extra = "Log in to your dashboard for more details."

        body = f"""
Hi {user.name},

{headline}

──────────────────────────────
  Booking # : {booking.booking_ref}
  Package   : {pkg_label} ({booking.pax} pax)
  Price     : S${booking.price}
  Event Date: {booking.event_date}
  Time      : {time_line}
  Venue     : {booking.event_venue}
  Status    : {new_status}
──────────────────────────────

{extra}

View your booking: https://bloomburrow.sg/dashboard

With love,
The Bloom Burrow Team 🌸
        """.strip()
        msg = Message(subject=subject, recipients=[user.email], body=body)
        mail.send(msg)
    except Exception as e:
        app.logger.warning(f"Could not send status update email: {e}")


# ── Password reset helpers ────────────────────────────────────────────────────

def generate_reset_token(email):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps(email, salt='password-reset')


def verify_reset_token(token, max_age=3600):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = s.loads(token, salt='password-reset', max_age=max_age)
    except (SignatureExpired, BadSignature):
        return None
    return email


# ── Routes ────────────────────────────────────────────────────────────────────

# ── Video streaming with range-request support (fixes Waitress disconnects) ──
@app.route('/static/videos/<path:filename>')
def serve_video(filename):
    video_path = os.path.join(BASE_DIR, 'static', 'videos', filename)
    if not os.path.isfile(video_path):
        return Response('Not found', status=404)

    file_size = os.path.getsize(video_path)
    range_header = request.headers.get('Range', None)

    if not range_header:
        # No range request — send whole file
        return send_file(video_path, mimetype='video/mp4')

    # Parse Range header, e.g. "bytes=0-1023"
    byte_start, byte_end = 0, file_size - 1
    match = range_header.replace('bytes=', '').split('-')
    if match[0]:
        byte_start = int(match[0])
    if match[1]:
        byte_end = int(match[1])
    byte_end = min(byte_end, file_size - 1)
    chunk_size = byte_end - byte_start + 1

    def generate():
        with open(video_path, 'rb') as f:
            f.seek(byte_start)
            remaining = chunk_size
            while remaining:
                read_size = min(65536, remaining)   # 64 KB chunks
                data = f.read(read_size)
                if not data:
                    break
                remaining -= len(data)
                yield data

    headers = {
        'Content-Range': f'bytes {byte_start}-{byte_end}/{file_size}',
        'Accept-Ranges': 'bytes',
        'Content-Length': str(chunk_size),
        'Content-Type': 'video/mp4',
    }
    return Response(generate(), status=206, headers=headers)


@app.route('/')
def index():
    return render_template('index.html', packages=PACKAGES)


@app.route('/packages')
def packages():
    return render_template('packages.html', packages=PACKAGES)


@app.route('/book/<package_key>', methods=['GET', 'POST'])
@login_required
def book(package_key):
    if package_key not in PACKAGES:
        flash('Invalid package selected.', 'error')
        return redirect(url_for('packages'))

    pkg = PACKAGES[package_key]

    if request.method == 'POST':
        event_date        = request.form.get('event_date', '').strip()
        event_start_time  = request.form.get('event_start_time', '').strip()
        event_end_time    = request.form.get('event_end_time', '').strip()
        event_venue       = request.form.get('event_venue', '').strip()
        phone             = request.form.get('phone', '').strip()
        notes             = request.form.get('notes', '').strip()
        wedding_table     = request.form.get('wedding_table_addon') == 'on'

        if not event_date or not event_venue or not phone or not event_start_time or not event_end_time:
            flash('Please fill in all required fields including event start and end time.', 'error')
            return render_template('book.html', pkg=pkg, package_key=package_key)

        # Validate end time is after start time
        if event_end_time <= event_start_time:
            flash('End time must be after start time.', 'error')
            return render_template('book.html', pkg=pkg, package_key=package_key)

        # Validate weekend only
        from datetime import datetime as dt
        try:
            d = dt.strptime(event_date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format.', 'error')
            return render_template('book.html', pkg=pkg, package_key=package_key)

        if d.weekday() < 5:  # 0–4 are Mon–Fri
            flash('We only accept bookings on weekends (Saturday & Sunday).', 'error')
            return render_template('book.html', pkg=pkg, package_key=package_key)

        # Check max 2 per day and no time overlap
        existing = Booking.query.filter_by(event_date=event_date).filter(
            Booking.status != 'Cancelled'
        ).all()

        if len(existing) >= 2:
            flash('Sorry, this date is fully booked. Please choose another weekend.', 'error')
            return render_template('book.html', pkg=pkg, package_key=package_key)

        for b in existing:
            if b.event_start_time and b.event_end_time:
                if event_start_time < b.event_end_time and b.event_start_time < event_end_time:
                    flash(
                        f'This time slot overlaps with an existing booking '
                        f'({b.event_start_time}–{b.event_end_time}). Please choose a different time.',
                        'error'
                    )
                    return render_template('book.html', pkg=pkg, package_key=package_key)

        final_price = pkg['price'] + (88 if wedding_table else 0)
        if wedding_table:
            addon_note = '[Add-on: Wedding Reception Table Styling +S$88]'
            notes = (addon_note + '\n' + notes).strip()

        booking = Booking(
            booking_ref=generate_booking_ref(),
            user_id=current_user.id,
            package=package_key,
            pax=pkg['pax'],
            price=final_price,
            event_date=event_date,
            event_start_time=event_start_time,
            event_end_time=event_end_time,
            event_venue=event_venue,
            phone=phone,
            notes=notes,
            status='Pending',
            payment_status='Awaiting Payment',
        )
        db.session.add(booking)
        db.session.commit()

        log_order_to_csv(booking, current_user, pkg)
        send_booking_notification(booking, current_user, pkg)
        send_booking_confirmation(booking, current_user, pkg)

        return redirect(url_for('payment', booking_id=booking.id))

    return render_template('book.html', pkg=pkg, package_key=package_key)


@app.route('/book/availability')
@login_required
def check_availability():
    date = request.args.get('date', '').strip()
    if not date:
        return jsonify({'error': 'No date provided'}), 400

    from datetime import datetime as dt
    try:
        d = dt.strptime(date, '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date'}), 400

    if d.weekday() < 5:
        return jsonify({'weekend': False, 'slots': [], 'count': 0})

    existing = Booking.query.filter_by(event_date=date).filter(
        Booking.status != 'Cancelled'
    ).all()

    slots = [
        {'start': b.event_start_time, 'end': b.event_end_time}
        for b in existing
        if b.event_start_time and b.event_end_time
    ]
    return jsonify({'weekend': True, 'count': len(existing), 'slots': slots})


@app.route('/payment/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def payment(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    if booking.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('dashboard'))

    pkg = PACKAGES[booking.package]

    if request.method == 'POST':
        file = request.files.get('screenshot')

        if not file or file.filename == '':
            flash('Please upload a screenshot of your payment.', 'error')
            return render_template('payment.html', booking=booking, pkg=pkg)

        if not allowed_file(file.filename) or not is_real_jpeg(file):
            flash('Only JPG/JPEG files are accepted for security reasons. Please take a screenshot and save it as a JPG.', 'error')
            return render_template('payment.html', booking=booking, pkg=pkg)

        ext      = file.filename.rsplit('.', 1)[1].lower()
        filename = f"payment_{booking.id}_{uuid.uuid4().hex[:8]}.{ext}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        booking.payment_screenshot = filename
        booking.payment_status     = 'Payment Submitted'
        db.session.commit()

        return redirect(url_for('booking_success', booking_id=booking.id))

    return render_template('payment.html', booking=booking, pkg=pkg)


@app.route('/booking-success/<int:booking_id>')
@login_required
def booking_success(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id:
        return redirect(url_for('dashboard'))
    pkg = PACKAGES[booking.package]
    return render_template('booking_success.html', booking=booking, pkg=pkg)


@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.created_at.desc()).all()
    # Count unread messages from admin per booking
    unread_counts = {
        b.id: ChatMessage.query.filter_by(booking_id=b.id, is_read=False)
                               .filter(ChatMessage.sender_id != current_user.id).count()
        for b in bookings
    }
    return render_template('dashboard.html', bookings=bookings, packages=PACKAGES, unread_counts=unread_counts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name     = request.form.get('name', '').strip()
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm  = request.form.get('confirm_password', '')

        if not name or not email or not password:
            flash('Please fill in all fields.', 'error')
        elif password != confirm:
            flash('Passwords do not match.', 'error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', 'error')
        elif User.query.filter_by(email=email).first():
            flash('An account with this email already exists.', 'error')
        else:
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            log_account_to_csv(user, plain_password=password)
            login_user(user)
            flash(f'Welcome, {name}! Your account has been created.', 'success')
            return redirect(url_for('dashboard'))

    return render_template('auth/register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        remember = request.form.get('remember') == 'on'

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        user  = User.query.filter_by(email=email).first()
        if user:
            token     = generate_reset_token(user.email)
            reset_url = url_for('reset_password', token=token, _external=True)
            try:
                msg = Message(
                    subject='🌸 Reset Your Bloom Burrow Password',
                    recipients=[user.email],
                    body=f"""Hi {user.name},

We received a request to reset your Bloom Burrow password.

Click the link below to set a new password (valid for 1 hour):
{reset_url}

If you didn't request this, you can safely ignore this email.

With love,
The Bloom Burrow Team 🌸
""".strip()
                )
                mail.send(msg)
            except Exception as e:
                app.logger.warning(f"Could not send password reset email: {e}")
        # Always show the same message to prevent email enumeration
        flash('If that email is registered, a reset link has been sent.', 'info')
        return redirect(url_for('login'))

    return render_template('auth/forgot_password.html')


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    email = verify_reset_token(token)
    if not email:
        flash('This reset link is invalid or has expired. Please request a new one.', 'error')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        password = request.form.get('password', '')
        confirm  = request.form.get('confirm_password', '')

        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'error')
        elif password != confirm:
            flash('Passwords do not match.', 'error')
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                user.set_password(password)
                db.session.commit()
                flash('Your password has been reset. Please log in.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Account not found.', 'error')
                return redirect(url_for('forgot_password'))

    return render_template('auth/reset_password.html', token=token)


# ── Admin routes ──────────────────────────────────────────────────────────────

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users           = User.query.filter_by(is_admin=False).order_by(User.created_at.desc()).all()
    bookings        = Booking.query.order_by(Booking.created_at.desc()).all()
    confirmed       = [b for b in bookings if b.status == 'Confirmed']
    total_revenue   = sum(b.price for b in confirmed)
    total_cost      = round(sum(b.cost or 0 for b in confirmed), 2)
    total_hours     = sum(b.hours_spent or 0 for b in confirmed)
    profit          = round(total_revenue - total_cost, 2)
    profit_per_hour = round(profit / total_hours, 2) if total_hours > 0 else 0
    pending_count   = sum(1 for b in bookings if b.payment_status == 'Payment Submitted')
    # Count unread messages from customers per booking
    unread_counts = {
        b.id: ChatMessage.query.filter_by(booking_id=b.id, is_read=False)
                               .filter(ChatMessage.sender_id != current_user.id).count()
        for b in bookings
    }
    total_unread = sum(unread_counts.values())
    return render_template(
        'admin/dashboard.html',
        users=users,
        bookings=bookings,
        packages=PACKAGES,
        total_revenue=total_revenue,
        total_cost=total_cost,
        total_hours=total_hours,
        profit=profit,
        profit_per_hour=profit_per_hour,
        pending_count=pending_count,
        unread_counts=unread_counts,
        total_unread=total_unread,
    )


@app.route('/admin/update-financials/<int:booking_id>', methods=['POST'])
@login_required
@admin_required
def admin_update_financials(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    try:
        booking.cost        = float(request.form.get('cost', 0) or 0)
        booking.hours_spent = float(request.form.get('hours_spent', 0) or 0)
        db.session.commit()
        flash(f'Financials saved for booking #{booking.booking_ref}.', 'success')
    except ValueError:
        flash('Invalid values — please enter numbers only.', 'error')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/update-status/<int:booking_id>', methods=['POST'])
@login_required
@admin_required
def admin_update_status(booking_id):
    booking    = Booking.query.get_or_404(booking_id)
    new_status = request.form.get('status')
    if new_status in ['Pending', 'Confirmed', 'Cancelled']:
        old_status = booking.status
        booking.status = new_status
        if new_status == 'Confirmed':
            booking.payment_status = 'Confirmed'
        elif new_status == 'Cancelled':
            booking.payment_status = 'Cancelled'
        db.session.commit()
        flash(f'Order #{booking.booking_ref} updated to {new_status}.', 'success')
        if new_status != old_status:
            send_status_update(booking, booking.user, new_status)
    return redirect(url_for('admin_dashboard'))


# ── Notification context processor ───────────────────────────────────────────

@app.context_processor
def inject_nav_notifications():
    """Inject unread chat counts into every template for the navbar bell."""
    if not current_user.is_authenticated:
        return dict(nav_notifications=[], nav_total_unread=0)
    try:
        base_q = db.session.query(
            Booking.id.label('booking_id'),
            Booking.booking_ref.label('booking_ref'),
            Booking.package.label('package'),
            Booking.event_date.label('event_date'),
            User.name.label('customer_name'),
            db.func.count(ChatMessage.id).label('unread')
        ).join(ChatMessage, ChatMessage.booking_id == Booking.id)\
         .join(User, User.id == Booking.user_id)\
         .filter(ChatMessage.is_read == False,
                 ChatMessage.sender_id != current_user.id)

        if not current_user.is_admin:
            base_q = base_q.filter(Booking.user_id == current_user.id)

        rows = base_q.group_by(Booking.id)\
                     .order_by(db.desc(db.func.max(ChatMessage.created_at)))\
                     .all()

        notifications = [{
            'booking_id':  r.booking_id,
            'booking_ref': r.booking_ref or str(r.booking_id),
            'label':       PACKAGES.get(r.package, {}).get('label', r.package),
            'date':        r.event_date,
            # Admin sees customer name; customer always sees "Admin"
            'chat_with':   r.customer_name if current_user.is_admin else 'Admin',
            'unread':      r.unread,
        } for r in rows]
        return dict(nav_notifications=notifications,
                    nav_total_unread=sum(n['unread'] for n in notifications))
    except Exception:
        return dict(nav_notifications=[], nav_total_unread=0)


@app.route('/notifications/poll')
@login_required
def notifications_poll():
    """AJAX endpoint polled by the navbar bell every few seconds."""
    try:
        base_q = db.session.query(
            Booking.id.label('booking_id'),
            Booking.booking_ref.label('booking_ref'),
            Booking.package.label('package'),
            Booking.event_date.label('event_date'),
            User.name.label('customer_name'),
            db.func.count(ChatMessage.id).label('unread')
        ).join(ChatMessage, ChatMessage.booking_id == Booking.id)\
         .join(User, User.id == Booking.user_id)\
         .filter(ChatMessage.is_read == False,
                 ChatMessage.sender_id != current_user.id)

        if not current_user.is_admin:
            base_q = base_q.filter(Booking.user_id == current_user.id)

        rows = base_q.group_by(Booking.id)\
                     .order_by(db.desc(db.func.max(ChatMessage.created_at)))\
                     .all()

        items = [{
            'booking_id':  r.booking_id,
            'booking_ref': r.booking_ref or str(r.booking_id),
            'label':       PACKAGES.get(r.package, {}).get('label', r.package),
            'date':        r.event_date,
            'chat_with':   r.customer_name if current_user.is_admin else 'Admin',
            'unread':      r.unread,
        } for r in rows]
        return jsonify({'total': sum(i['unread'] for i in items), 'items': items})
    except Exception:
        return jsonify({'total': 0, 'items': []})


# ── Chat routes ───────────────────────────────────────────────────────────────

@app.route('/chat/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def chat(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    # Only the booking owner or admin can access this chat
    if not current_user.is_admin and booking.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        body = request.form.get('body', '').strip()
        if not body:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'ok': False}), 400
            return redirect(url_for('chat', booking_id=booking_id))

        msg = ChatMessage(booking_id=booking_id, sender_id=current_user.id, body=body)
        db.session.add(msg)

        # Mark all unread messages from the other side as read on reply
        ChatMessage.query.filter_by(booking_id=booking_id, is_read=False).filter(
            ChatMessage.sender_id != current_user.id
        ).update({'is_read': True})
        db.session.commit()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'ok':     True,
                'id':     msg.id,
                'body':   msg.body,
                'sender': msg.sender.name,
                'time':   msg.created_at.strftime('%d %b, %H:%M'),
                'is_mine': True,
            })
        return redirect(url_for('chat', booking_id=booking_id))

    # Mark incoming messages as read when opening the page
    ChatMessage.query.filter_by(booking_id=booking_id, is_read=False).filter(
        ChatMessage.sender_id != current_user.id
    ).update({'is_read': True})
    db.session.commit()

    messages = ChatMessage.query.filter_by(booking_id=booking_id)\
                                .order_by(ChatMessage.created_at.asc()).all()
    pkg = PACKAGES[booking.package]
    return render_template('chat.html', booking=booking, pkg=pkg, messages=messages, packages=PACKAGES)


@app.route('/chat/<int:booking_id>/poll')
@login_required
def chat_poll(booking_id):
    """AJAX endpoint — returns messages newer than ?after=<id>"""
    booking = Booking.query.get_or_404(booking_id)
    if not current_user.is_admin and booking.user_id != current_user.id:
        return jsonify([]), 403

    after_id = request.args.get('after', 0, type=int)
    msgs = ChatMessage.query.filter_by(booking_id=booking_id)\
                            .filter(ChatMessage.id > after_id)\
                            .order_by(ChatMessage.created_at.asc()).all()

    # Mark fetched messages as read
    for m in msgs:
        if m.sender_id != current_user.id:
            m.is_read = True
    db.session.commit()

    return jsonify([{
        'id':     m.id,
        'body':   m.body,
        'sender': m.sender.name,
        'time':   m.created_at.strftime('%d %b, %H:%M'),
        'is_mine': m.sender_id == current_user.id,
    } for m in msgs])


# ── Init ──────────────────────────────────────────────────────────────────────

with app.app_context():
    db.create_all()

    # Migrate: add any missing columns to existing databases
    from sqlalchemy import inspect, text
    inspector    = inspect(db.engine)
    user_cols    = [c['name'] for c in inspector.get_columns('user')]
    booking_cols = [c['name'] for c in inspector.get_columns('booking')]

    with db.engine.connect() as conn:
        if 'is_admin' not in user_cols:
            conn.execute(text('ALTER TABLE user ADD COLUMN is_admin BOOLEAN DEFAULT 0'))
        if 'payment_status' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN payment_status VARCHAR(30) DEFAULT 'Awaiting Payment'"))
        if 'payment_screenshot' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN payment_screenshot VARCHAR(300) DEFAULT ''"))
        if 'booking_ref' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN booking_ref VARCHAR(4)"))
        if 'phone' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN phone VARCHAR(20) DEFAULT ''"))
        if 'cost' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN cost FLOAT DEFAULT 0.0"))
        if 'hours_spent' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN hours_spent FLOAT DEFAULT 0.0"))
        if 'event_start_time' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN event_start_time VARCHAR(5) DEFAULT ''"))
        if 'event_end_time' not in booking_cols:
            conn.execute(text("ALTER TABLE booking ADD COLUMN event_end_time VARCHAR(5) DEFAULT ''"))
        conn.commit()

    # Backfill booking_ref for any existing bookings that don't have one
    for b in Booking.query.filter(Booking.booking_ref == None).all():
        b.booking_ref = generate_booking_ref()
    db.session.commit()

    # Create admin account if it doesn't exist, or update password if it does
    admin_user = User.query.filter_by(email='admin').first()
    if not admin_user:
        admin_user = User(name='Admin', email='admin', is_admin=True)
        db.session.add(admin_user)
    admin_user.set_password('JYVS2026')
    db.session.commit()


if __name__ == '__main__':
    port  = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='127.0.0.1', port=port, debug=debug, threaded=True)
