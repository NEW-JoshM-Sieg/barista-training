import json
from pathlib import Path

questions = json.loads(Path(__file__).with_name("quiz.json").read_text())
score = 0
for i, item in enumerate(questions, 1):
    print(f"\n{i}. {item['q']}")
    for n, option in enumerate(item["options"]):
        print(f"   {n + 1}) {option}")
    if input("Answer: ").strip() == str(item["answer"] + 1):
        score += 1
print(f"\nScore: {score}/{len(questions)}")
