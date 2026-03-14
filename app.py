from flask import Flask, render_template, request
from agent import evaluate_document
from docx import Document

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = ""
    filename = ""
    word_count = ""
    risk_score = ""
    summary = ""

    if request.method == "POST":

        file = request.files["file"]
        filename = file.filename

        # Read DOCX properly
        if filename.endswith(".docx"):
            doc = Document(file)
            content = "\n".join([para.text for para in doc.paragraphs])
        else:
            content = file.read().decode("utf-8", errors="ignore")

        analysis = evaluate_document(content)

        result = analysis["result"]
        word_count = analysis["word_count"]
        risk_score = analysis["risk_score"]
        summary = analysis["summary"]

    return render_template(
        "index.html",
        result=result,
        filename=filename,
        word_count=word_count,
        risk_score=risk_score,
        summary=summary
    )

if  __name__== "__main__":
    app.run(debug=True)