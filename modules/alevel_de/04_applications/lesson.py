TITLE = "Applications of Differential Equations"

SECTIONS = [
    {
        "title": "Modelling with Differential Equations",
        "body": """
<h3>Setting Up Models</h3>
<p>Many real-world phenomena lead to differential equations:</p>

<p><strong>Newton's Second Law:</strong> \(F = ma = m\\frac{dv}{dt}\) (force-mass-acceleration)</p>
<p><strong>Exponential growth/decay:</strong> \(\\frac{dN}{dt} = kN\) (population, radioactivity)</p>
<p><strong>Cooling/heating:</strong> \(\\frac{dT}{dt} = k(T - T_{\\text{ambient}})\) (Newton's Law of Cooling)</p>

<div class="worked-example">
<h4>Example 6: Exponential Decay</h4>
<p>A radioactive substance decays at a rate proportional to its amount. If 100 g remains after 10 years and 80 g after 20 years, find the half-life.</p>
<p><strong>Solution:</strong> Let N(t) = amount at time t. The model is \(\\frac{dN}{dt} = -kN\) (negative = decay)</p>
<p>This is separable: \(\\frac{1}{N}\,dN = -k\,dt \Rightarrow \ln|N| = -kt + C\)</p>
<p>\(N(t) = N_0 e^{-kt}\), where \(N_0\) is initial amount</p>
<p>From conditions: \(N(10) = 100\), \(N(20) = 80\)</p>
<p>\(100 = N_0 e^{-10k}\) and \(80 = N_0 e^{-20k}\)</p>
<p>Dividing: \(\\frac{100}{80} = e^{10k} \Rightarrow \\frac{5}{4} = e^{10k} \Rightarrow k = \\frac{\ln(5/4)}{10} \\approx 0.0223\) per year</p>
<p>Half-life: \(t_{1/2}\) where \(N(t_{1/2}) = N_0/2 \Rightarrow e^{-kt_{1/2}} = \\frac{1}{2} \Rightarrow t_{1/2} = \\frac{\ln 2}{k} \\approx 31\) years</p>
</div>

<div class="worked-example">
<h4>Example 7: Newton's Law of Cooling</h4>
<p>A cup of tea at 95°C is placed in a room at 20°C. After 5 minutes, it cools to 75°C. When will it reach 40°C?</p>
<p><strong>Solution:</strong> \(\\frac{dT}{dt} = k(T - 20)\), where k is a constant</p>
<p>This is linear: \(\\frac{dT}{dt} - kT = -20k\)</p>
<p>Using integrating factor: \(T(t) = 20 + Ce^{kt}\)</p>
<p>\(T(0) = 95\): \(95 = 20 + C \Rightarrow C = 75\), so \(T(t) = 20 + 75e^{kt}\)</p>
<p>\(T(5) = 75\): \(75 = 20 + 75e^{5k} \Rightarrow e^{5k} = \\frac{11}{15} \Rightarrow k = \\frac{\ln(11/15)}{5} \\approx -0.0675\)</p>
<p>\(T(t) = 20 + 75e^{-0.0675t}\)</p>
<p>Find t when \(T = 40\): \(40 = 20 + 75e^{-0.0675t} \Rightarrow e^{-0.0675t} = \\frac{4}{15}\)</p>
<p>\(t = -\\frac{\ln(4/15)}{0.0675} \\approx 18.4\) minutes</p>
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
