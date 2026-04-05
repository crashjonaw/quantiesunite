TITLE = "Applications of Differential Equations"

SECTIONS = [
    {
        "title": "Modelling with Differential Equations",
        "body": """
<h3>Setting Up Models</h3>
<p>Many real-world phenomena lead to differential equations:</p>

<p><strong>Newton's Second Law:</strong> F = ma = m(dv/dt) (force-mass-acceleration)</p>
<p><strong>Exponential growth/decay:</strong> dN/dt = kN (population, radioactivity)</p>
<p><strong>Cooling/heating:</strong> dT/dt = k(T - T_ambient) (Newton's Law of Cooling)</p>

<div class="worked-example">
<h4>Example 6: Exponential Decay</h4>
<p>A radioactive substance decays at a rate proportional to its amount. If 100 g remains after 10 years and 80 g after 20 years, find the half-life.</p>
<p><strong>Solution:</strong> Let N(t) = amount at time t. The model is dN/dt = -kN (negative = decay)</p>
<p>This is separable: (1/N)dN = -k dt ⟹ ln|N| = -kt + C</p>
<p>N(t) = N₀e^(-kt), where N₀ is initial amount</p>
<p>From conditions: N(10) = 100, N(20) = 80</p>
<p>100 = N₀e^(-10k) and 80 = N₀e^(-20k)</p>
<p>Dividing: 100/80 = e^(10k) ⟹ 5/4 = e^(10k) ⟹ k = ln(5/4)/10 ≈ 0.0223 per year</p>
<p>Half-life: t₁/₂ where N(t₁/₂) = N₀/2 ⟹ e^(-kt₁/₂) = 1/2 ⟹ t₁/₂ = ln(2)/k ≈ 31 years</p>
</div>

<div class="worked-example">
<h4>Example 7: Newton's Law of Cooling</h4>
<p>A cup of tea at 95°C is placed in a room at 20°C. After 5 minutes, it cools to 75°C. When will it reach 40°C?</p>
<p><strong>Solution:</strong> dT/dt = k(T - 20), where k is a constant</p>
<p>This is linear: dT/dt - kT = -20k</p>
<p>Using integrating factor: T(t) = 20 + Ce^(kt)</p>
<p>T(0) = 95: 95 = 20 + C ⟹ C = 75, so T(t) = 20 + 75e^(kt)</p>
<p>T(5) = 75: 75 = 20 + 75e^(5k) ⟹ e^(5k) = 11/15 ⟹ k = ln(11/15)/5 ≈ -0.0675</p>
<p>T(t) = 20 + 75e^(-0.0675t)</p>
<p>Find t when T = 40: 40 = 20 + 75e^(-0.0675t) ⟹ e^(-0.0675t) = 4/15</p>
<p>t = -ln(4/15)/0.0675 ≈ 18.4 minutes</p>
</div>

<h3>Validating Solutions</h3>
<p>Always check that the solution:</p>
<ol>
<li>Satisfies the differential equation (substitute back)</li>
<li>Satisfies initial conditions if given</li>
<li>Makes physical sense (reasonable units, sign, limiting behavior)</li>
</ol>
"""
    }
]
