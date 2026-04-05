"""
Migrate lesson.py files to use LaTeX for all mathematical expressions.
Wraps math patterns in \\( ... \\) delimiters inside Python string literals.

Usage: python3 generated_questions/migrate_lesson_latex.py [--dry-run]
"""
import re
import os
import sys
import glob

# Patterns already in LaTeX — skip these
ALREADY_LATEX = re.compile(r'\\\\?\(|\\\\?\)|\\frac|\\sqrt|\\times|\\div|\$[^$]+\$')

def apply_latex_to_line(line):
    """Apply LaTeX wrapping to a single line of HTML content."""
    # Skip lines that are pure Python (not inside string literals)
    stripped = line.strip()
    if stripped.startswith(('TITLE', 'SECTIONS', 'def ', 'import ', '#', ']', '[', '{', '}', 'class ')):
        return line
    # Skip lines already heavily LaTeX'd
    if line.count('\\(') > 2 or line.count('\\\\(') > 2:
        return line

    # Split on existing LaTeX blocks to avoid double-wrapping
    parts = re.split(r'(\\\\?\(.*?\\\\?\)|\$[^$]+\$)', line)

    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # This is an existing LaTeX block — keep as-is
            result.append(part)
            continue

        # Apply patterns to non-LaTeX parts
        text = part

        # Arithmetic: "3 + 5 = 8", "12 × 3", "45 ÷ 9"
        text = re.sub(r'(?<![\\$a-zA-Z>])(\d[\d,]*\s*[+\-×÷]\s*\d[\d,]*(?:\s*[+\-×÷=]\s*\d[\d,]*)*)(?![<\\$])', r'\\(\1\\)', text)

        # Fractions: "3/4" (but not dates or paths)
        text = re.sub(r'(?<![\\$/a-zA-Z])(\d+/\d+)(?![a-zA-Z/\\$])', r'\\(\1\\)', text)

        # Powers with unicode: x², 5³, cm²
        text = re.sub(r'(?<![\\$])(\w+[²³⁴⁵⁶⁷⁸⁹⁰]+)', lambda m: '\\(' + m.group(1).replace('²','^2').replace('³','^3').replace('⁴','^4').replace('⁵','^5').replace('⁶','^6').replace('⁷','^7').replace('⁸','^8').replace('⁹','^9').replace('⁰','^0') + '\\)', text)

        # Powers with caret: x^2, (a+b)^n
        text = re.sub(r'(?<![\\$])(\(?[a-zA-Z0-9+\-]+\)?\^\{?[a-zA-Z0-9/+\-]+\}?)', r'\\(\1\\)', text)

        # Variable equations: "x = 5", "n = 10", "y = 2x + 3"
        text = re.sub(r'(?<![\\$a-zA-Z"=])([a-z]\s*=\s*[\d\.\-][^<,]{0,20}?)(?=[,.<\s]|$)', r'\\(\1\\)', text)

        # Inequality: "x < 5", "n > 0", "n ≥ 10"
        text = re.sub(r'(?<![\\$])([a-z]\s*[<>≤≥≠]\s*\d+)', r'\\(\1\\)', text)

        # Unicode symbols
        text = text.replace('×', '\\times ')
        text = text.replace('÷', '\\div ')
        text = text.replace('π', '\\pi ')
        text = text.replace('θ', '\\theta ')
        text = text.replace('λ', '\\lambda ')
        text = text.replace('σ', '\\sigma ')
        text = text.replace('μ', '\\mu ')
        text = text.replace('∞', '\\infty ')

        # Wrap any remaining bare unicode-replaced operators that aren't in \( \)
        text = re.sub(r'(?<!\\[(\s])\\times\s', r'\\(\\times\\) ', text)
        text = re.sub(r'(?<!\\[(\s])\\div\s', r'\\(\\div\\) ', text)

        # Clean up double-wrapping
        text = text.replace('\\(\\(', '\\(').replace('\\)\\)', '\\)')

        result.append(text)

    return ''.join(result)


def process_file(filepath, dry_run=False):
    """Process a single lesson.py file."""
    with open(filepath) as f:
        content = f.read()

    # Only process inside string literals (between triple quotes)
    lines = content.split('\n')
    in_string = False
    new_lines = []
    changes = 0

    for line in lines:
        if '"""' in line or "'''" in line:
            count = line.count('"""') + line.count("'''")
            if count == 1:
                in_string = not in_string
            # If opening a string, process from after the quotes
            # If closing, process up to the quotes

        if in_string and '<' in line:
            # This line is HTML content inside a string — process it
            new_line = apply_latex_to_line(line)
            if new_line != line:
                changes += 1
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if changes > 0 and not dry_run:
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_lines))

    return changes


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN ===\n")

    files = sorted(glob.glob('modules/*/lesson.py') + glob.glob('modules/*/*/lesson.py'))
    total_changes = 0
    files_changed = 0

    for f in files:
        changes = process_file(f, dry_run)
        if changes > 0:
            files_changed += 1
            total_changes += changes
            short = f.replace('modules/', '')
            if files_changed <= 20:
                print(f"  {short}: {changes} lines changed")

    if files_changed > 20:
        print(f"  ... and {files_changed - 20} more files")

    print(f"\nTotal: {total_changes} lines changed across {files_changed} files")
    if dry_run:
        print("(No changes saved — run without --dry-run to apply)")
