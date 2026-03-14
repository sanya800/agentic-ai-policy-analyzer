from utils import load_rules

def evaluate_document(content):

    rules = load_rules()
    text = content.lower()

    word_count = len(text.split())
    violations = []

    # Check restricted words
    for word in rules["restricted_words"]:
        if word in text:
            violations.append(word)

    # Risk score
    risk_score = len(violations) * 20

    # Simple summary (first 20 words)
    summary = " ".join(content.split()[:20])

    if violations:
        result = f"⚠ Violations: {', '.join(violations)}"
    else:
        result = "✅ Document follows policy"

    return {
        "result": result,
        "word_count": word_count,
        "risk_score": risk_score,
        "summary": summary
    }