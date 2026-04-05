"""
Insert generated questions into the database.
Usage: python3 generated_questions/insert_questions.py generated_questions/<filename>.json
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
    for topic_id, questions in data.items():
        existing = db.get_question_count(topic_id)
        if existing >= 100:
            print(f"  {topic_id}: already has {existing} questions, skipping")
            continue

        # Avoid duplicates by checking question text
        all_existing = db.get_all_questions(topic_id)
        existing_texts = {q["question"].strip().lower() for q in all_existing}

        new_questions = []
        for q in questions:
            if q["question"].strip().lower() not in existing_texts:
                # Sanitize fields
                diff = q.get("difficulty", 1)
                if isinstance(diff, list):
                    diff = diff[0] if diff else 1
                q["difficulty"] = int(diff) if isinstance(diff, (int, float, str)) else 1
                if isinstance(q.get("tags"), str):
                    q["tags"] = [q["tags"]]
                if isinstance(q.get("concept"), list):
                    q["concept"] = ", ".join(str(x) for x in q["concept"])
                if isinstance(q.get("explanation"), list):
                    q["explanation"] = " ".join(str(x) for x in q["explanation"]) if q["explanation"] else ""
                if not isinstance(q.get("explanation"), str):
                    q["explanation"] = str(q.get("explanation", ""))
                new_questions.append(q)
                existing_texts.add(q["question"].strip().lower())

        if new_questions:
            db.insert_questions(topic_id, new_questions)
            total += len(new_questions)
            print(f"  {topic_id}: inserted {len(new_questions)} new questions (total now: {existing + len(new_questions)})")
        else:
            print(f"  {topic_id}: all questions already exist, skipping")

    print(f"\nTotal inserted: {total}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 insert_questions.py <file.json>")
        sys.exit(1)
    insert_from_file(sys.argv[1])
