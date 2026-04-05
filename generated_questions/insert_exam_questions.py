"""
Insert generated exam questions into the exam_questions table.
Usage: python3 generated_questions/insert_exam_questions.py generated_questions/<filename>.json
"""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import database as db

def insert_from_file(filepath):
    with open(filepath) as f:
        data = json.load(f)

    total = 0
    for exam_id, questions in data.items():
        # Group questions by topic_id for insertion
        by_topic = {}
        for q in questions:
            tid = q.get("topic_id", exam_id)
            if tid not in by_topic:
                by_topic[tid] = []
            by_topic[tid].append(q)

        # Check existing to avoid duplicates
        for tid, qs in by_topic.items():
            existing = db.get_all_exam_questions(tid)
            existing_texts = {q["question"].strip().lower() for q in existing}

            new_questions = []
            for q in qs:
                # Sanitize fields
                diff = q.get("difficulty", 2)
                if isinstance(diff, list):
                    diff = diff[0] if diff else 2
                q["difficulty"] = int(diff) if isinstance(diff, (int, float, str)) else 2

                if isinstance(q.get("tags"), str):
                    q["tags"] = [q["tags"]]
                if isinstance(q.get("concept"), list):
                    q["concept"] = ", ".join(str(x) for x in q["concept"])
                if isinstance(q.get("explanation"), list):
                    q["explanation"] = " ".join(str(x) for x in q["explanation"]) if q["explanation"] else ""
                if not isinstance(q.get("explanation"), str):
                    q["explanation"] = str(q.get("explanation", ""))

                if q["question"].strip().lower() not in existing_texts:
                    new_questions.append(q)
                    existing_texts.add(q["question"].strip().lower())

            if new_questions:
                db.insert_exam_questions(tid, new_questions)
                total += len(new_questions)
                print(f"  {exam_id}/{tid}: inserted {len(new_questions)} exam questions")

    print(f"\nTotal exam questions inserted: {total}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 insert_exam_questions.py <file.json>")
        sys.exit(1)
    insert_from_file(sys.argv[1])
