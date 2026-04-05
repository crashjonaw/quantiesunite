"""Export questions to JSON files for LaTeX conversion by agents."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.core import get_db

def export_table(table, output_dir):
    db = get_db()
    rows = db.execute(f"SELECT * FROM {table} ORDER BY topic_id, id").fetchall()
    db.close()

    by_topic = {}
    for r in rows:
        tid = r["topic_id"]
        if tid not in by_topic:
            by_topic[tid] = []
        opts = r["options"]
        if isinstance(opts, str):
            try: opts = json.loads(opts)
            except: opts = []
        by_topic[tid].append({
            "id": r["id"],
            "question": r["question"],
            "answer": r["answer"],
            "options": opts or [],
            "explanation": r["explanation"] or "",
        })

    os.makedirs(output_dir, exist_ok=True)
    for tid, qs in by_topic.items():
        path = os.path.join(output_dir, f"{tid}.json")
        with open(path, "w") as f:
            json.dump(qs, f, indent=2)
    print(f"Exported {len(rows)} questions from {table} across {len(by_topic)} topics")

export_table("quiz_questions", "generated_questions/latex_quiz")
export_table("exam_questions", "generated_questions/latex_exam")
