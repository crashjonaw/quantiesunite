"""Reimport LaTeX-converted questions back into the database.
Matches by original question ID if present, otherwise by question text."""
import json, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.core import get_db

def reimport(input_dir, table):
    db = get_db()
    total = 0
    errors = 0

    # Build lookup of all existing questions by ID and by text
    all_rows = db.execute(f"SELECT id, topic_id, question FROM {table}").fetchall()
    by_text = {}
    for r in all_rows:
        by_text[r["question"].strip().lower()] = r["id"]

    for fpath in sorted(glob.glob(os.path.join(input_dir, "*.json"))):
        topic_id = os.path.splitext(os.path.basename(fpath))[0]
        with open(fpath) as f:
            questions = json.load(f)

        # Get original questions for this topic to match by position
        originals = db.execute(
            f"SELECT id, question FROM {table} WHERE topic_id=? ORDER BY id",
            (topic_id,)).fetchall()

        for i, q in enumerate(questions):
            opts = json.dumps(q.get("options", [])) if q.get("options") else "[]"
            explanation = q.get("explanation", "")
            if isinstance(explanation, list):
                explanation = " ".join(str(x) for x in explanation)

            qid = q.get("id")
            if not qid and i < len(originals):
                # Match by position
                qid = originals[i]["id"]

            if qid:
                db.execute(
                    f"UPDATE {table} SET question=?, answer=?, options=?, explanation=? WHERE id=?",
                    (q["question"], q["answer"], opts, explanation, qid))
                total += 1
            else:
                errors += 1

    db.commit()
    db.close()
    print(f"Updated {total} questions in {table}" + (f" ({errors} unmatched)" if errors else ""))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 reimport_latex.py <input_dir> <table_name>")
        sys.exit(1)
    reimport(sys.argv[1], sys.argv[2])
