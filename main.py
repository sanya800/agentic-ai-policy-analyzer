from agent import evaluate_document

print("=== Autonomous Policy Compliance Agent ===")
print("Paste your document below (Press Enter twice to submit):\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

document_text = "\n".join(lines)

result = evaluate_document(document_text)

print("\n===== Evaluation Result =====")
print(f"Word Count: {result['word_count']}")
print(f"Minimum Required: {result['min_words_required']}")
print(f"Missing Fields: {result['missing_fields']}")
print(f"Restricted Words Found: {result['restricted_words_found']}")
print(f"Compliance Score: {result['compliance_score']}%")
print(f"Final Decision: {result['final_decision']}")