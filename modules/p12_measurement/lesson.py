"""Measurement (length, mass, volume) — Lesson sections."""

SECTIONS = [
    {
        "title": "What is Measurement? Why Do We Measure?",
        "body": """<p>Measurement is about finding out <strong>how big, how heavy, or how much space</strong> something takes up.</p>
<p>We measure so we can compare, understand, and communicate information about the world around us!</p>
<svg viewBox="0 0 410 150" style="width:100%;max-width:410px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="120" height="120" fill='rgba(65,105,225,0.15)' stroke='#4169E1' stroke-width='2' rx='4'/>
  <text x="75" y="45" font-size='13' font-weight='bold' fill='#4169E1' text-anchor='middle'>LENGTH</text>
  <text x="75" y="70" font-size='11' fill='currentColor' text-anchor='middle'>How long?</text>
  <text x="75" y="88" font-size='11' fill='currentColor' text-anchor='middle'>How tall?</text>
  <text x="75" y="106" font-size='11' fill='currentColor' text-anchor='middle'>How far?</text>

  <rect x="150" y="15" width="120" height="120" fill='rgba(245,158,11,0.15)' stroke='#f59e0b' stroke-width='2' rx='4'/>
  <text x="210" y="45" font-size='13' font-weight='bold' fill='#f59e0b' text-anchor='middle'>MASS</text>
  <text x="210" y="70" font-size='11' fill='currentColor' text-anchor='middle'>How heavy?</text>
  <text x="210" y="88" font-size='11' fill='currentColor' text-anchor='middle'>How much</text>
  <text x="210" y="106" font-size='11' fill='currentColor' text-anchor='middle'>does it weigh?</text>

  <rect x="285" y="15" width="120" height="120" fill='rgba(34,197,94,0.15)' stroke='#22c55e' stroke-width='2' rx='4'/>
  <text x="345" y="45" font-size='13' font-weight='bold' fill='#22c55e' text-anchor='middle'>VOLUME</text>
  <text x="345" y="70" font-size='11' fill='currentColor' text-anchor='middle'>How much</text>
  <text x="345" y="88" font-size='11' fill='currentColor' text-anchor='middle'>liquid?</text>
  <text x="345" y="106" font-size='11' fill='currentColor' text-anchor='middle'>How full?</text>
</svg>
<div class='example-box'>
<strong>Real-world examples:</strong><br>
A pencil is 19 cm long<br>
An apple weighs 200 grams<br>
A glass holds 250 milliliters of water
</div>
<p><strong>Why measure?</strong> We measure to:</p>
<ul style="margin-left: 20px;">
<li>Cook recipes (need exact amounts)</li>
<li>Buy clothes (need the right size)</li>
<li>Build things (need precise measurements)</li>
<li>Play sports (need to know distances)</li>
<li>Keep track of growth</li>
</ul>"""
    },
    {
        "title": "Length: Meters and Centimeters",
        "body": """<p><strong>Length</strong> measures how long or how far something is. The main units are meters (m) and centimeters (cm).</p>
<p><strong>1 meter = 100 centimeters</strong></p>
<svg viewBox="0 0 390 230" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="30" font-size='14' font-weight='bold' fill='currentColor'>Understanding the meter:</text>

  <rect x="15" y="45" width="360" height="30" fill='rgba(65,105,225,0.18)' stroke='#4169E1' stroke-width='2' rx='4'/>
  <text x="195" y="65" font-size='12' font-weight='bold' fill='currentColor' text-anchor='middle'>1 meter (m) = 100 centimeters</text>

  <text x="15" y="105" font-size='13' fill='currentColor'>A meter is about:</text>
  <text x="30" y="130" font-size='12' fill='currentColor'>The height of a doorway</text>
  <text x="30" y="150" font-size='12' fill='currentColor'>The width of a door</text>
  <text x="30" y="170" font-size='12' fill='currentColor'>The height of a tall 7-year-old child</text>

  <line x1="15" y1="190" x2="375" y2="190" stroke='#22c55e' stroke-width='1' stroke-dasharray='5'/>
  <text x="15" y="215" font-size='12' fill='currentColor'>A centimeter is about the width of your thumb!</text>
</svg>
<div class='example-box'>
<strong>Common length measurements:</strong><br>
A book: about 20 cm<br>
A pencil: about 19 cm<br>
A ruler: 30 cm<br>
A room: about 4-5 meters<br>
A school field: about 100 meters
</div>
<p><strong>How to measure:</strong> Use a ruler or measuring tape. Line up the 0 mark with the start, then read where it ends!</p>"""
    },
    {
        "title": "Mass and Weight: Grams and Kilograms",
        "body": """<p><strong>Mass</strong> tells us how heavy something is. We measure mass in grams (g) and kilograms (kg).</p>
<p><strong>1 kilogram = 1000 grams</strong></p>
<svg viewBox="0 0 390 250" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="30" font-size='14' font-weight='bold' fill='currentColor'>Understanding grams and kilograms:</text>

  <rect x="15" y="45" width="170" height="80" fill='rgba(245,158,11,0.15)' stroke='#f59e0b' stroke-width='2' rx='4'/>
  <text x="30" y="70" font-size='12' font-weight='bold' fill='currentColor'>GRAM (g)</text>
  <text x="30" y="90" font-size='11' fill='currentColor'>Very light!</text>
  <text x="30" y="108" font-size='11' fill='currentColor'>Like a few grains of rice</text>

  <rect x="205" y="45" width="170" height="80" fill='rgba(34,197,94,0.15)' stroke='#22c55e' stroke-width='2' rx='4'/>
  <text x="220" y="70" font-size='12' font-weight='bold' fill='currentColor'>KILOGRAM (kg)</text>
  <text x="220" y="90" font-size='11' fill='currentColor'>Much heavier!</text>
  <text x="220" y="108" font-size='11' fill='currentColor'>1 kg = 1000 grams</text>

  <text x="15" y="155" font-size='13' font-weight='bold' fill='currentColor'>Real-world examples:</text>
  <text x="30" y="180" font-size='12' fill='currentColor'>An apple: about 200 grams</text>
  <text x="30" y="200" font-size='12' fill='currentColor'>A child: about 30 kilograms</text>
  <text x="30" y="220" font-size='12' fill='currentColor'>A large book: about 1 kilogram</text>
  <text x="30" y="240" font-size='12' fill='currentColor'>An adult: about 60-80 kilograms</text>
</svg>
<div class='example-box'>
<strong>Remembering the difference:</strong><br>
<br>
Grams (g) = Light things (food, small items)<br>
Kilograms (kg) = Heavy things (people, furniture)<br>
<br>
Think: "kilo-" means 1000, so 1 kg = 1000 g!
</div>
<p><strong>How to measure:</strong> Use a weighing scale. Place the object on the scale and read the number!</p>"""
    },
    {
        "title": "Volume and Capacity: Liters and Milliliters",
        "body": """<p><strong>Volume</strong> (or capacity) measures how much liquid something can hold, or how much space something takes up.</p>
<p><strong>1 liter = 1000 milliliters</strong></p>
<svg viewBox="0 0 390 280" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="30" font-size='14' font-weight='bold' fill='currentColor'>Understanding liters and milliliters:</text>

  <rect x="25" y="50" width="70" height="100" fill='rgba(65,105,225,0.18)' stroke='#4169E1' stroke-width='2' rx='4'/>
  <rect x="25" y="90" width="70" height="60" fill='rgba(65,105,225,0.35)' stroke='none' rx='4'/>
  <text x="60" y="120" font-size='11' font-weight='bold' fill='currentColor' text-anchor='middle'>1 L</text>

  <rect x="135" y="70" width="45" height="80" fill='rgba(34,197,94,0.18)' stroke='#22c55e' stroke-width='2' rx='4'/>
  <rect x="135" y="110" width="45" height="40" fill='rgba(34,197,94,0.35)' stroke='none' rx='4'/>
  <text x="157" y="130" font-size='10' font-weight='bold' fill='currentColor' text-anchor='middle'>1 mL</text>

  <text x="215" y="90" font-size='13' fill='currentColor'>1 liter = 1000 mL</text>
  <text x="215" y="115" font-size='12' fill='currentColor'>A liter is</text>
  <text x="215" y="135" font-size='12' fill='currentColor'>1000 times bigger</text>
  <text x="215" y="155" font-size='12' fill='currentColor'>than 1 milliliter!</text>

  <text x="15" y="190" font-size='13' font-weight='bold' fill='currentColor'>Real-world examples:</text>
  <text x="30" y="215" font-size='12' fill='currentColor'>A glass of milk: about 200 mL</text>
  <text x="30" y="235" font-size='12' fill='currentColor'>A water bottle: about 500 mL to 1 L</text>
  <text x="30" y="255" font-size='12' fill='currentColor'>A bucket: about 10 liters</text>
  <text x="30" y="275" font-size='12' fill='currentColor'>A bathtub: about 100-200 liters</text>
</svg>
<div class='example-box'>
<strong>Remembering the units:</strong><br>
<br>
Milliliters (mL) = Small amounts (medicine, juice in a cup)<br>
Liters (L) = Larger amounts (milk in a jug, water in a bucket)<br>
1 milliliter is 1/1000 of a liter
</div>
<p><strong>How to measure:</strong> Use a measuring cup or graduated cylinder. Pour the liquid and read where the top of the liquid level reaches!</p>"""
    },
    {
        "title": "Comparing and Estimating Measurements",
        "body": """<p>Now that we know different units, we can <strong>estimate</strong> (make a good guess) and <strong>compare</strong> measurements!</p>
<p>Estimation is a valuable skill that helps us check if our answers make sense.</p>
<svg viewBox="0 0 390 300" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="30" font-size='14' font-weight='bold' fill='currentColor'>Estimation examples:</text>

  <rect x="15" y="45" width="360" height="55" fill='rgba(245,158,11,0.12)' stroke='#f59e0b' stroke-width='1' rx='4'/>
  <text x="30" y="68" font-size='12' fill='currentColor'>Question: "How tall is your teacher?"</text>
  <text x="30" y="88" font-size='12' fill='currentColor'>Estimate: About 170 cm (or about 1.7 meters)</text>

  <rect x="15" y="115" width="360" height="55" fill='rgba(34,197,94,0.12)' stroke='#22c55e' stroke-width='1' rx='4'/>
  <text x="30" y="138" font-size='12' fill='currentColor'>Question: "How heavy is a backpack full of books?"</text>
  <text x="30" y="158" font-size='12' fill='currentColor'>Estimate: About 5-10 kilograms</text>

  <rect x="15" y="185" width="360" height="55" fill='rgba(65,105,225,0.12)' stroke='#4169E1' stroke-width='1' rx='4'/>
  <text x="30" y="208" font-size='12' fill='currentColor'>Question: "How much juice in a box?"</text>
  <text x="30" y="228" font-size='12' fill='currentColor'>Estimate: About 200 or 250 milliliters</text>

  <text x="15" y="270" font-size='13' font-weight='bold' fill='currentColor'>Tips for good estimations:</text>
  <text x="30" y="290" font-size='11' fill='currentColor'>1. Use reference objects you know (a ruler is 30 cm)</text>
</svg>
<div class='example-box'>
<strong>Comparing measurements:</strong><br>
<br>
Is 150 cm longer than 1 meter?<br>
Think: 1 meter = 100 cm, so 150 cm > 100 cm. YES!<br>
<br>
Is a 500g apple heavier than a 1 kg apple?<br>
Think: 1 kg = 1000 g, so 500 g < 1000 g. NO!
</div>
<p><strong>Practice tip:</strong> Estimate a measurement, then actually measure it. See how close your estimate was!</p>"""
    }
]
