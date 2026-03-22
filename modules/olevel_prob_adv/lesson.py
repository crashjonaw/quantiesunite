SECTIONS = [
    {
        "title": "Sample Space and Probability Basics",
        "body": """
        <h3>Foundations of Probability</h3>
        <p><strong>Probability</strong> is the likelihood of an event occurring, expressed as a fraction, decimal, or percentage.</p>

        <h4>Basic Formula</h4>
        <p style="text-align: center;"><strong>P(A) = (Number of favorable outcomes) / (Total number of possible outcomes)</strong></p>

        <h4>Sample Space</h4>
        <p>The <strong>sample space</strong> is the set of all possible outcomes of an experiment.</p>

        <div class="example-box">
            <p><strong>Example 1:</strong> Rolling a die</p>
            <ul>
                <li>Sample space: {1, 2, 3, 4, 5, 6}</li>
                <li>P(rolling a 4) = 1/6</li>
                <li>P(rolling an even number) = 3/6 = 1/2</li>
            </ul>
        </div>

        <h4>Key Properties</h4>
        <ul>
            <li>0 ≤ P(A) ≤ 1</li>
            <li>P(A) = 0 means event is impossible</li>
            <li>P(A) = 1 means event is certain</li>
            <li>P(A) + P(A') = 1, where A' is the complement of A</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 2:</strong> Drawing a card from a standard deck</p>
            <p>P(drawing a red card) = 26/52 = 1/2</p>
            <p>P(not drawing a red card) = 1 − 1/2 = 1/2</p>
        </div>
        """
    },
    {
        "title": "Tree Diagrams",
        "body": """
        <h3>Visual Representation of Multi-Step Events</h3>
        <p>A <strong>tree diagram</strong> shows all possible outcomes when an experiment has multiple stages.</p>

        <h4>Structure</h4>
        <ul>
            <li>Start with a single point (root)</li>
            <li>Draw branches for each possible outcome of the first event</li>
            <li>From each endpoint, draw branches for the next event</li>
            <li>Label branches with probabilities</li>
            <li>End outcomes are at the leaf nodes</li>
        </ul>

        <h4>Calculating Probabilities</h4>
        <p><strong>Multiplication Rule:</strong> Probability of a path = product of probabilities along that path</p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Flip a coin, then roll a die</p>
            <ul>
                <li>First flip: P(H) = 1/2, P(T) = 1/2</li>
                <li>Then roll: P(any number) = 1/6</li>
                <li>P(H and rolling a 4) = 1/2 × 1/6 = 1/12</li>
                <li>P(T and rolling an even) = 1/2 × 3/6 = 1/4</li>
            </ul>
        </div>

        <h4>With and Without Replacement</h4>
        <p><strong>Without replacement:</strong> Item is not returned; probabilities change</p>
        <p><strong>With replacement:</strong> Item is returned; probabilities stay the same</p>

        <div class="example-box">
            <p><strong>Example 4:</strong> Drawing two balls from a bag of 3 red and 2 blue</p>
            <p><strong>Without replacement:</strong></p>
            <ul>
                <li>P(first red) = 3/5</li>
                <li>P(second red | first red) = 2/4 = 1/2 (only 2 red left)</li>
                <li>P(both red) = 3/5 × 2/4 = 6/20 = 3/10</li>
            </ul>
            <p><strong>With replacement:</strong></p>
            <ul>
                <li>P(first red) = 3/5</li>
                <li>P(second red | first red) = 3/5 (unchanged)</li>
                <li>P(both red) = 3/5 × 3/5 = 9/25</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Conditional Probability",
        "body": """
        <h3>Probability Given That Something Else Occurred</h3>
        <p><strong>Conditional probability</strong> is the probability of event A given that event B has already occurred.</p>

        <h4>Formula</h4>
        <p style="text-align: center;"><strong>P(A|B) = P(A and B) / P(B)</strong></p>
        <p>Read as "P of A given B"</p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Drawing cards</p>
            <p>What's the probability the second card is a heart, given the first card was a heart (no replacement)?</p>
            <p>P(2nd heart | 1st heart) = 12/51 (12 hearts left out of 51 cards)</p>
        </div>

        <h4>Independence vs. Dependence</h4>
        <p><strong>Independent events:</strong> P(A|B) = P(A). Event B doesn't affect event A.</p>
        <p><strong>Dependent events:</strong> P(A|B) ≠ P(A). Event B changes the probability of A.</p>

        <div class="example-box">
            <p><strong>Example 6:</strong> Is "rolling a 4" independent of "flipping heads"?</p>
            <p>P(rolling 4) = 1/6</p>
            <p>P(rolling 4 | heads) = 1/6 (coin flip doesn't affect die roll)</p>
            <p>Since P(4) = P(4|H), these events are independent.</p>
        </div>

        <h4>For Independent Events</h4>
        <p style="text-align: center;"><strong>P(A and B) = P(A) × P(B)</strong></p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Flip two coins</p>
            <p>P(both heads) = P(H) × P(H) = 1/2 × 1/2 = 1/4</p>
        </div>
        """
    },
    {
        "title": "Mutually Exclusive and Non-Mutually Exclusive Events",
        "body": """
        <h3>Adding Probabilities</h3>

        <h4>Mutually Exclusive Events</h4>
        <p>Events are <strong>mutually exclusive</strong> if they cannot occur at the same time.</p>

        <p style="text-align: center;"><strong>P(A or B) = P(A) + P(B)</strong></p>

        <div class="example-box">
            <p><strong>Example 8:</strong> Rolling a die</p>
            <p>P(rolling a 3 or rolling a 5) = 1/6 + 1/6 = 2/6 = 1/3</p>
            <p>These cannot occur simultaneously, so they're mutually exclusive.</p>
        </div>

        <h4>Non-Mutually Exclusive Events</h4>
        <p>Events can occur together. Use the <strong>Addition Rule:</strong></p>
        <p style="text-align: center;"><strong>P(A or B) = P(A) + P(B) − P(A and B)</strong></p>

        <p>We subtract P(A and B) to avoid counting the overlap twice.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Drawing a card from a deck</p>
            <p>P(red card OR ace) = ?</p>
            <p>P(red) = 26/52, P(ace) = 4/52, P(red and ace) = 2/52</p>
            <p>P(red or ace) = 26/52 + 4/52 − 2/52 = 28/52 = 7/13</p>
        </div>

        <h4>Complement Rule</h4>
        <p style="text-align: center;"><strong>P(A or A') = 1</strong></p>
        <p style="text-align: center;"><strong>P(A) + P(A') = 1</strong></p>

        <p>Often easier to find P(not A) and subtract from 1.</p>

        <div class="example-box">
            <p><strong>Example 10:</strong> Drawing a card</p>
            <p>P(not an ace) = 1 − P(ace) = 1 − 4/52 = 48/52 = 12/13</p>
        </div>
        """
    },
    {
        "title": "Combined Probability Problems",
        "body": """
        <h3>Complex Scenarios</h3>

        <h4>Using Tree Diagrams for Complex Problems</h4>
        <p>Combine conditional probabilities systematically using tree diagrams.</p>

        <div class="example-box">
            <p><strong>Example 11:</strong> A factory has machines A and B. A produces 60% of items, B produces 40%. A has 2% defect rate, B has 5% defect rate. Find P(defective item).</p>
            <p>Tree branches:
            <ul>
                <li>From A: P(A) = 0.6, P(defective|A) = 0.02</li>
                <li>From B: P(B) = 0.4, P(defective|B) = 0.05</li>
            </ul>
            <p>P(defective) = P(from A and defective) + P(from B and defective)</p>
            <p>= 0.6 × 0.02 + 0.4 × 0.05</p>
            <p>= 0.012 + 0.020 = 0.032 = 3.2%</p>
        </div>

        <h4>Bayes' Theorem (Reverse Conditional)</h4>
        <p>Find probability of cause given an effect:</p>
        <p style="text-align: center;"><strong>P(A|B) = P(B|A) × P(A) / P(B)</strong></p>

        <div class="example-box">
            <p><strong>Example 12:</strong> From Example 11, if we find a defective item, what's the probability it came from machine A?</p>
            <p>P(A|defective) = P(defective|A) × P(A) / P(defective)</p>
            <p>= 0.02 × 0.6 / 0.032</p>
            <p>= 0.012 / 0.032 = 3/8 = 0.375 = 37.5%</p>
        </div>

        <h4>Verification with Frequency Tables</h4>
        <p>For complex problems, use a two-way frequency table to organize data.</p>

        <div class="example-box">
            <p><strong>Example 13:</strong> Survey of 200 people on coffee/tea preference and time of day</p>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">Coffee</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">Tea</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">Total</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;">Morning</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">90</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">40</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">130</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;">Afternoon</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">30</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">40</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">70</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;">Total</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">120</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">80</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">200</td>
                </tr>
            </table>
            <p>P(coffee) = 120/200 = 0.6</p>
            <p>P(afternoon | coffee) = 30/120 = 0.25</p>
        </div>
        """
    }
]
