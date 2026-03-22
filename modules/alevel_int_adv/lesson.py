"""Integration (advanced) — Lesson sections."""

SECTIONS = [
    {"title": "The Fundamental Theorem of Calculus",
     "body": """<p>The FTC links differentiation and integration — they are inverse operations.</p>
     <div class='example-box'>If F'(x) = f(x), then ∫[a to b] f(x) dx = F(b) − F(a)</div>
     <p>This means to find a definite integral, find the antiderivative and evaluate at the bounds.</p>"""},
    {"title": "Integration by substitution (u-substitution)",
     "body": """<p>Use substitution when the integrand contains a function and its derivative.</p>
     <div class='example-box'>∫ 2x(x²+1)⁵ dx<br>
     Let u = x²+1, then du = 2x dx<br>
     = ∫ u⁵ du = u⁶/6 + C = (x²+1)⁶/6 + C</div>"""},
    {"title": "Integration by parts",
     "body": """<p>For products of different function types, use:</p>
     <div class='example-box'>∫ u dv = uv − ∫ v du</div>
     <p><strong>LIATE rule</strong> for choosing u: Logarithm, Inverse trig, Algebraic, Trig, Exponential.</p>
     <div class='example-box'>∫ x·eˣ dx<br>
     u = x → du = dx; dv = eˣ dx → v = eˣ<br>
     = x·eˣ − ∫ eˣ dx = x·eˣ − eˣ + C = eˣ(x−1) + C</div>"""},
]
