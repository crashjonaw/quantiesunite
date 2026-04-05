TITLE = "Complex Probability: Synthesis & Bayes' Theorem"

SECTIONS = [
    {
        "title": "Combining Concepts: Multi-Stage Problems",
        "body": """
        <h3>Bringing It All Together</h3>
        <p>Real-world probability problems rarely fit neatly into a single category. They require combining multiple concepts: tree diagrams, conditional probability, addition rules, and complements. The key is systematic organization.</p>

        <h4>Strategy for Complex Problems</h4>
        <ol>
            <li><strong>Identify the structure:</strong> Are events sequential (use tree)? Simultaneous (use addition rule)?</li>
            <li><strong>Determine dependencies:</strong> Does the outcome of one event affect the next?</li>
            <li><strong>Draw and label:</strong> Use a tree diagram, table, or area model to organize information</li>
            <li><strong>Calculate step-by-step:</strong> Multiply along paths, add across them</li>
            <li><strong>Check reasonableness:</strong> Does your answer make sense? Is it between 0 and 1?</li>
        </ol>

        <h4>The Law of Total Probability (Partition Rule)</h4>
        <p>When an experiment naturally splits into mutually exclusive cases that cover all possibilities, the total probability is the sum of probabilities from each path.</p>

        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>P(Event) = P(Event | Case 1) × P(Case 1) + P(Event | Case 2) × P(Case 2) + ...</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Sum over all mutually exclusive, exhaustive cases</p>
        </div>

        <div class="worked-example">
            <h4>Example 1: Factory with Multiple Production Lines</h4>
            <p><strong>Setup:</strong></p>
            <ul>
                <li>Machine A produces 60% of items (defect rate: 2%)</li>
                <li>Machine B produces 40% of items (defect rate: 5%)</li>
            </ul>
            <p><strong>Question:</strong> What's the probability a randomly selected item is defective?</p>

            <p><strong>Solution using Law of Total Probability:</strong></p>
            <ul>
                <li>P(Defective) = P(Defective | From A) × P(From A) + P(Defective | From B) × P(From B)</li>
                <li>= 0.02 × 0.60 + 0.05 × 0.40</li>
                <li>= 0.012 + 0.020</li>
                <li>= 0.032 or 3.2%</li>
            </ul>

            <p><strong>Tree diagram view:</strong></p>
            <ul>
                <li>Path 1: From A (prob 0.60) → Defective (prob 0.02) = 0.012</li>
                <li>Path 2: From B (prob 0.40) → Defective (prob 0.05) = 0.020</li>
                <li>Total: 0.012 + 0.020 = 0.032</li>
            </ul>

            <p><strong>Interpretation:</strong> Even though A has a low defect rate, the overall defect rate is 3.2% because we're mixing both machines.</p>
        </div>

        <div class="concept-box">
            <h4>Example 2: Testing for Disease (With Unequal Prevalence)</h4>
            <p><strong>Setup:</strong> A disease affects 1% of the population. A test correctly identifies 95% of infected people and 90% of uninfected people.</p>
            <p><strong>Question:</strong> If a random person tests positive, what's the probability they actually have the disease?</p>

            <p><strong>This is Bayes' theorem (next section), but we can solve it with total probability first:</strong></p>
            <p>P(Test Positive) = P(Test Pos | Has Disease) × P(Has Disease) + P(Test Pos | No Disease) × P(No Disease)</p>
            <p>= 0.95 × 0.01 + 0.10 × 0.99</p>
            <p>= 0.0095 + 0.099</p>
            <p>= 0.1085 or 10.85%</p>

            <p><strong>Insight:</strong> Even though the test is "95% accurate," only 10.85% of positive tests indicate actual disease! This is because the disease is rare.</p>
        </div>

        <h4>Organizing with Frequency Tables</h4>
        <p>For complex multi-outcome problems, a two-way (or higher-dimensional) table organizes information clearly.</p>

        <div class="concept-box">
            <h4>Example 3: Survey Data Organization</h4>
            <p><strong>Survey of 200 people:</strong></p>
            <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
                <tr class="formula-box">
                    <td style="padding: 10px;"><strong>Beverage / Time</strong></td>
                    <td style="padding: 10px;"><strong>Morning</strong></td>
                    <td style="padding: 10px;"><strong>Afternoon</strong></td>
                    <td style="padding: 10px;"><strong>Total</strong></td>
                </tr>
                <tr >
                    <td style="padding: 10px;"><strong>Coffee</strong></td>
                    <td style="padding: 10px;">90</td>
                    <td style="padding: 10px;">30</td>
                    <td style="padding: 10px;">120</td>
                </tr>
                <tr >
                    <td style="padding: 10px;"><strong>Tea</strong></td>
                    <td style="padding: 10px;">40</td>
                    <td style="padding: 10px;">40</td>
                    <td style="padding: 10px;">80</td>
                </tr>
                <tr class="formula-box">
                    <td style="padding: 10px;"><strong>Total</strong></td>
                    <td style="padding: 10px;">130</td>
                    <td style="padding: 10px;">70</td>
                    <td style="padding: 10px;">200</td>
                </tr>
            </table>

            <p><strong>From this table, we can quickly find:</strong></p>
            <ul>
                <li>P(Coffee) = 120/200 = 0.60</li>
                <li>P(Afternoon | Coffee) = 30/120 = 0.25</li>
                <li>P(Coffee | Morning) = 90/130 ≈ 0.692</li>
                <li>P(Coffee and Morning) = 90/200 = 0.45</li>
            </ul>

            <p><strong>Why tables help:</strong> All information in one place. Easy to count overlaps. Simple to verify using totals.</p>
        </div>
        """
    },
    {
        "title": "Bayes' Theorem: Reversing the Conditional",
        "body": """
        <h3>Finding the Cause When You Know the Effect</h3>
        <p>Sometimes we observe an outcome and want to find the probability of its cause. For example: "I tested positive for a disease. What's the probability I actually have it?" This requires reversing the conditional probability—a job for Bayes' Theorem.</p>

        <h4>The Formula</h4>
        <div style="text-align: center; border-radius: 8px; padding: 20px; margin: 20px 0">
            <p style="font-size: 1.1em; margin: 0"><strong>P(A | B) = [P(B | A) × P(A)] / P(B)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Probability of cause A given observed effect B</p>
        </div>

        <p><strong>Breaking it down:</strong></p>
        <ul>
            <li><strong>P(A|B)</strong> = what we want (probability of cause given effect)</li>
            <li><strong>P(B|A)</strong> = likelihood of observing effect if cause is true (usually given)</li>
            <li><strong>P(A)</strong> = prior probability of the cause (base rate)</li>
            <li><strong>P(B)</strong> = total probability of observing the effect (from all possible causes)</li>
        </ul>

        <p><strong>Key insight:</strong> P(B) is found using the Law of Total Probability.</p>

        <div class="worked-example">
            <h4>Example 4: Medical Testing</h4>
            <p><strong>Scenario:</strong></p>
            <ul>
                <li>Disease prevalence: 1% of population</li>
                <li>Test sensitivity (catches the disease): 99% (if you have it, test is positive with probability 0.99)</li>
                <li>Test specificity (no false positives): 95% (if you don't have it, test is negative with probability 0.95)</li>
            </ul>

            <p><strong>Question:</strong> You test positive. What's the probability you actually have the disease?</p>

            <p><strong>Setup:</strong></p>
            <ul>
                <li>A = "You have the disease" → P(A) = 0.01</li>
                <li>B = "Test is positive"</li>
                <li>P(B|A) = 0.99 (sensitivity: test catches disease 99% of the time)</li>
                <li>P(B|A') = 0.05 (false positive rate: 1 − specificity)</li>
            </ul>

            <p><strong>Step 1: Calculate P(B) using Law of Total Probability</strong></p>
            <p>P(B) = P(B|A) × P(A) + P(B|A') × P(A')</p>
            <p>= 0.99 × 0.01 + 0.05 × 0.99</p>
            <p>= 0.0099 + 0.0495</p>
            <p>= 0.0594</p>

            <p><strong>Step 2: Apply Bayes' Theorem</strong></p>
            <p>P(A|B) = [P(B|A) × P(A)] / P(B)</p>
            <p>= [0.99 × 0.01] / 0.0594</p>
            <p>= 0.0099 / 0.0594</p>
            <p>≈ 0.167 or 16.7%</p>

            <p><strong>Shocking result:</strong> Even with a positive test, there's only a 16.7% chance you actually have the disease! The disease is so rare that false positives outnumber true positives.</p>
        </div>

        <div class="concept-box">
            <h4>Example 5: Factory Machines (Revisited with Bayes)</h4>
            <p><strong>From earlier:</strong></p>
            <ul>
                <li>P(From A) = 0.60, P(Defective | A) = 0.02</li>
                <li>P(From B) = 0.40, P(Defective | B) = 0.05</li>
                <li>P(Defective) = 0.032</li>
            </ul>

            <p><strong>New question:</strong> If a defective item is found, what's the probability it came from machine A?</p>

            <p><strong>Solution:</strong></p>
            <p>P(From A | Defective) = [P(Defective | A) × P(A)] / P(Defective)</p>
            <p>= [0.02 × 0.60] / 0.032</p>
            <p>= 0.012 / 0.032</p>
            <p>= 0.375 or 37.5%</p>

            <p><strong>Interpretation:</strong> If you find a defective item, it's more likely (62.5%) to be from machine B, even though B produces fewer items. Why? Because B has a higher defect rate.</p>
        </div>

        <h4>Intuition Behind Bayes</h4>
        <p>Bayes' Theorem updates our belief (prior probability) based on evidence (the observed event). The more diagnostic the evidence (how differently the effect behaves under A vs. not-A), the more the posterior probability shifts from the prior.</p>

        <p><strong>The lesson:</strong> Base rates matter. A rare cause won't become likely just because one diagnostic test says it's present. Always consider how common the cause is to begin with.</p>
        """
    },
    {
        "title": "Putting It Together: Complete Worked Examples",
        "body": """
        <h3>Complex, Multi-Step Problems</h3>
        <p>This section shows how all pieces fit together in realistic problems.</p>

        <div class="worked-example">
            <h4>Example 6: Multi-Draw Without Replacement</h4>
            <p><strong>Scenario:</strong> A bag contains 4 red, 5 blue, and 3 yellow balls (12 total). Two balls are drawn without replacement.</p>

            <p><strong>Question:</strong> What's the probability that both balls are the same color?</p>

            <p><strong>Solution:</strong></p>
            <p>P(same color) = P(both red) + P(both blue) + P(both yellow)</p>

            <p><strong>P(both red):</strong></p>
            <ul>
                <li>1st draw: P(Red) = 4/12</li>
                <li>2nd draw (given 1st was red): P(Red) = 3/11</li>
                <li>P(both red) = 4/12 × 3/11 = 12/132</li>
            </ul>

            <p><strong>P(both blue):</strong></p>
            <ul>
                <li>P(both blue) = 5/12 × 4/11 = 20/132</li>
            </ul>

            <p><strong>P(both yellow):</strong></p>
            <ul>
                <li>P(both yellow) = 3/12 × 2/11 = 6/132</li>
            </ul>

            <p><strong>Total:</strong></p>
            <p>P(same color) = 12/132 + 20/132 + 6/132 = 38/132 = 19/66 ≈ 0.288</p>

            <p><strong>Check:</strong> Verify with the complement: P(different colors) = 1 − 19/66 = 47/66 ✓</p>
        </div>

        <div class="concept-box">
            <h4>Example 7: Decision Tree with Multiple Stages</h4>
            <p><strong>Scenario:</strong> A student has a 70% chance of passing an exam if they study (which they do 80% of the time) and a 30% chance if they don't study.</p>

            <p><strong>Question a:</strong> What's the probability they pass?</p>
            <ul>
                <li>Path 1 (Study and Pass): 0.8 × 0.7 = 0.56</li>
                <li>Path 2 (Don't Study and Pass): 0.2 × 0.3 = 0.06</li>
                <li>P(Pass) = 0.56 + 0.06 = 0.62</li>
            </ul>

            <p><strong>Question b:</strong> Given that the student passed, what's the probability they studied?</p>
            <p>P(Studied | Passed) = P(Passed | Studied) × P(Studied) / P(Passed)</p>
            <p>= [0.7 × 0.8] / 0.62</p>
            <p>= 0.56 / 0.62</p>
            <p>≈ 0.903 or 90.3%</p>

            <p><strong>Interpretation:</strong> Passing is strong evidence that the student studied (90.3% likely). Even though they had a 70% pass rate with studying and 30% without, the combination of a good pass rate and frequent studying makes a passing exam a strong indicator of studying.</p>
        </div>

        <h4>General Approach to Complex Problems</h4>
        <ol>
            <li><strong>Identify random variables:</strong> What are we uncertain about?</li>
            <li><strong>List given probabilities:</strong> What do we know?</li>
            <li><strong>Identify the question:</strong> What are we asked to find?</li>
            <li><strong>Choose tools:</strong> Tree diagram? Table? Addition rule? Bayes?</li>
            <li><strong>Execute systematically:</strong> Show each step; use fractions until the end</li>
            <li><strong>Check the answer:</strong> Is it between 0 and 1? Does it make intuitive sense?</li>
        </ol>

        <p><strong>Final insight:</strong> Probability is about organizing information logically and computing carefully. Master the concepts—sample space, tree diagrams, conditioning, overlap, and Bayes—and you can solve nearly any probability problem.</p>
        """
    }
]
