import os
from flask import Flask, render_template, request
from rag_core import answer_from_pdf
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        pdf = request.files["pdf"]
        question = request.form["question"]

        pdf_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(pdf_path)

        answer = answer_from_pdf(
            pdf_path=pdf_path,
            question=question,
            api_key=os.getenv("GROQ_API_KEY")
        )

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
