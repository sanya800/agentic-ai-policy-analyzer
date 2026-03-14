import json

def load_rules():
    with open("rules.json", "r") as file:
        return json.load(file)

def count_words(text):
    return len(text.split())

def check_required_fields(text, required_fields):
    missing = []
    for field in required_fields:
        if field.lower() not in text.lower():
            missing.append(field)
    return missing

def check_restricted_words(text, restricted_words):
    found = []
    for word in restricted_words:
        if word.lower() in text.lower():
            found.append(word)
    return found