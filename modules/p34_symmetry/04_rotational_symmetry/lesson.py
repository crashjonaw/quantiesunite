TITLE = "Rotational Symmetry"

SECTIONS = [
    {
        "title": "What is Rotational Symmetry?",
        "body": """
        <h3>Definition</h3>
        <p><strong>Rotational symmetry</strong> means a shape looks <strong>the same after rotating it</strong> (turning it) around a central point, without flipping it.</p>

        <div class="concept-box">
            <p><strong>Key Difference from Reflective Symmetry:</strong> You turn the shape, not flip it. Imagine spinning a shape like a wheel.</p>
        </div>

        <h3>Example: A Square</h3>
        <p>If you rotate a square 90° (a quarter turn), it looks exactly the same!</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 500 150" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
                <!-- Original square -->
                <rect x="40" y="40" width="80" height="80" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>
                <circle cx="80" cy="80" r="3" fill='#fbbf24'/>
                <text x="80" y="135" text-anchor='middle' fill='currentColor' font-size='11'>0°</text>

                <!-- 90° rotation -->
                <rect x="190" y="40" width="80" height="80" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>
                <circle cx="230" cy="80" r="3" fill='#fbbf24'/>
                <text x="230" y="135" text-anchor='middle' fill='currentColor' font-size='11'>90°</text>

                <!-- 180° rotation -->
                <rect x="340" y="40" width="80" height="80" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>
                <circle cx="380" cy="80" r="3" fill='#fbbf24'/>
                <text x="380" y="135" text-anchor='middle' fill='currentColor' font-size='11'>180°</text>

                <text x="250" y="30" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>All look identical!</text>
            </svg>
        </div>

        <p><strong>Notice:</strong> All three squares look exactly the same. This is rotational symmetry!</p>
        """
    },
    {
        "title": "Order of Rotational Symmetry",
        "body": """
        <h3>What is the Order?</h3>
        <p>The <strong>order of rotational symmetry</strong> is the number of times a shape looks identical when rotated 360° (a full turn).</p>

        <div class="worked-example">
            <p><strong>Example: Square</strong></p>
            <p>A square looks identical at:</p>
            <ul>
                <li>90° (after 1/4 turn)</li>
                <li>180° (after 1/2 turn)</li>
                <li>270° (after 3/4 turn)</li>
                <li>360° (after full turn, back to start)</li>
            </ul>
            <p><strong>Order = 4</strong> (4 times during a 360° rotation)</p>
        </div>

        <h3>Common Orders</h3>

        <table style="width:100%;margin:20px 0;border-collapse:collapse;">
            <tr style="background:#1e293b;">
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Shape</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: center">Order</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Angle Between Identical Positions</th>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Equilateral Triangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">3</td>
                <td style="border:1px solid #475569;padding:10px;">120°</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Square</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">4</td>
                <td style="border:1px solid #475569;padding:10px;">90°</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Regular Pentagon</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">5</td>
                <td style="border:1px solid #475569;padding:10px;">72°</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Regular Hexagon</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">6</td>
                <td style="border:1px solid #475569;padding:10px;">60°</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Circle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">∞</td>
                <td style="border:1px solid #475569;padding:10px;">Any angle</td>
            </tr>
        </table>

        <h3>Formula for Order</h3>
        <div class="concept-box">
            <p>Order = 360° ÷ (angle of rotation for identical shape)</p>
            <p><strong>Example:</strong> Square rotates 90° and looks the same → 360° ÷ 90° = 4</p>
        </div>
        """
    },
    {
        "title": "Rotational Symmetry in Different Shapes",
        "body": """
        <h3>Equilateral Triangle: Order 3</h3>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 500 180" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
                <!-- 0° -->
                <polygon points="80,140 50,60 110,60" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>
                <circle cx="80" cy="85" r="2" fill='#fbbf24'/>
                <text x="80" y="160" text-anchor='middle' fill='currentColor' font-size='11'>0°</text>

                <!-- 120° -->
                <polygon points="230,140 200,60 260,60" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>
                <circle cx="230" cy="85" r="2" fill='#fbbf24'/>
                <text x="230" y="160" text-anchor='middle' fill='currentColor' font-size='11'>120°</text>

                <!-- 240° -->
                <polygon points="380,140 350,60 410,60" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>
                <circle cx="380" cy="85" r="2" fill='#fbbf24'/>
                <text x="380" y="160" text-anchor='middle' fill='currentColor' font-size='11'>240°</text>

                <text x="250" y="30" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Equilateral Triangle: Order 3 (rotations of 120°)</text>
            </svg>
        </div>

        <h3>Letter "S": Order 2</h3>
        <p>The letter S looks the same when rotated 180°.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 350 180" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- 0° -->
                <text x="80" y="90" fill='#60a5fa' font-size='48' font-weight='bold'>S</text>
                <circle cx="80" cy="80" r="2" fill='#fbbf24'/>
                <text x="80" y="150" text-anchor='middle' fill='currentColor' font-size='11'>0°</text>

                <!-- 180° -->
                <text x="260" y="90" fill='#60a5fa' font-size='48' font-weight='bold' transform='rotate(180 260 80)'>S</text>
                <circle cx="260" cy="80" r="2" fill='#fbbf24'/>
                <text x="260" y="150" text-anchor='middle' fill='currentColor' font-size='11'>180°</text>

                <text x="175" y="30" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Letter S: Order 2</text>
            </svg>
        </div>

        <h3>Rectangle: Order 2</h3>
        <p>A rectangle looks the same when rotated 180°, but NOT at 90°.</p>

        <div class="warning-box">
            <p><strong>Important:</strong> Rectangles have rotational symmetry of order 2 (180° rotation), but NOT 4. Squares are different — they have order 4.</p>
        </div>
        """
    },
    {
        "title": "Reflective vs. Rotational Symmetry",
        "body": """
        <h3>Side-by-Side Comparison</h3>

        <table style="width:100%;margin:20px 0;border-collapse:collapse;">
            <tr style="background:#1e293b;">
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Feature</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Reflective Symmetry</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Rotational Symmetry</th>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;"><strong>How it works</strong></td>
                <td style="border:1px solid #475569;padding:10px;">Fold or flip along a line</td>
                <td style="border:1px solid #475569;padding:10px;">Turn or rotate around a point</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;"><strong>Mirror image?</strong></td>
                <td style="border:1px solid #475569;padding:10px;">Yes (one half mirrors the other)</td>
                <td style="border:1px solid #475569;padding:10px;">No (same orientation)</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;"><strong>Measurement</strong></td>
                <td style="border:1px solid #475569;padding:10px;">Number of lines of symmetry</td>
                <td style="border:1px solid #475569;padding:10px;">Order of rotational symmetry</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;"><strong>Example: Square</strong></td>
                <td style="border:1px solid #475569;padding:10px;">4 lines of symmetry</td>
                <td style="border:1px solid #475569;padding:10px;">Order 4 (90°, 180°, 270°, 360°)</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;"><strong>Example: Rectangle</strong></td>
                <td style="border:1px solid #475569;padding:10px;">2 lines of symmetry</td>
                <td style="border:1px solid #475569;padding:10px;">Order 2 (180°, 360°)</td>
            </tr>
        </table>

        <h3>Can a Shape Have Both?</h3>
        <p><strong>Yes!</strong> Many shapes have both reflective and rotational symmetry.</p>

        <div class="success-box">
            <p><strong>Square:</strong> Has both 4 lines of reflective symmetry AND rotational symmetry of order 4.</p>
            <p><strong>Equilateral triangle:</strong> Has both 3 lines of reflective symmetry AND rotational symmetry of order 3.</p>
            <p><strong>Rectangle:</strong> Has both 2 lines of reflective symmetry AND rotational symmetry of order 2.</p>
        </div>

        <h3>Can a Shape Have Rotational But Not Reflective?</h3>
        <p><strong>Yes!</strong> Some shapes have rotational symmetry but NO reflective symmetry.</p>

        <div class="concept-box">
            <p><strong>Example: A swastika or pinwheel shape</strong> — has rotational symmetry of order 4, but no lines of reflective symmetry.</p>
        </div>
        """
    },
    {
        "title": "Identifying Rotational Symmetry: The Tracing Method",
        "body": """
        <h3>How to Find the Order of Rotational Symmetry</h3>

        <div class="worked-example">
            <p><strong>Method 1: Mental Rotation</strong></p>
            <ul>
                <li>Imagine rotating the shape slowly by small amounts.</li>
                <li>Count how many times it looks identical during a full 360° turn.</li>
                <li>That number is the order.</li>
            </ul>

            <p><strong>Method 2: Tracing Paper Method (Hands-On)</strong></p>
            <ul>
                <li>Trace the shape onto a piece of paper.</li>
                <li>Mark the center point with a pin.</li>
                <li>Rotate the paper slowly around the pin.</li>
                <li>Count how many times the traced shape matches the original shape.</li>
            </ul>
        </div>

        <h3>Practice Example: Regular Hexagon</h3>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 400 295" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
                <!-- Regular hexagon with labeled vertices -->
                <polygon points="200,50 280,100 280,200 200,250 120,200 120,100" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Vertices -->
                <circle cx="200" cy="50" r="4" fill='#fbbf24'/>
                <text x="200" y="35" text-anchor='middle' fill='#fbbf24' font-size='11'>A</text>

                <circle cx="280" cy="100" r="4" fill='#fbbf24'/>
                <text x="295" y="100" text-anchor='middle' fill='#fbbf24' font-size='11'>B</text>

                <circle cx="280" cy="200" r="4" fill='#fbbf24'/>
                <text x="295" y="200" text-anchor='middle' fill='#fbbf24' font-size='11'>C</text>

                <!-- Center -->
                <circle cx="200" cy="150" r="3" fill='#ef4444'/>

                <text x="200" y="280" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Regular Hexagon: Rotate 60° each time → Order 6</text>
            </svg>
        </div>

        <p>A regular hexagon has 6 sides and rotates 60° each time it looks identical:</p>
        <ul>
            <li>60°: Vertex A moves to where B was → identical!</li>
            <li>120°: Vertex A moves further → identical!</li>
            <li>180°, 240°, 300°, 360°: All identical!</li>
        </ul>

        <p><strong>Order = 6</strong></p>
        """
    }
]
