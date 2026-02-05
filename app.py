import os
from flask import Flask, render_template, request, session
from rag_core import answer_from_pdf
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)
app.secret_key = "documind-ai-secret"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔥 Allow up to 10 MB PDFs (IMPORTANT FOR RENDER)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None

    # 🔹 Fresh load → reset session
    if request.method == "GET":
        session.clear()
        return render_template("index.html")

    question = request.form.get("question", "").strip()

    # 🔹 Handle PDF upload (ONLY if user selected one)
    if "pdf" in request.files:
        pdf = request.files["pdf"]

        if pdf and pdf.filename != "":
            filename = secure_filename(pdf.filename)
            pdf_path = os.path.join(UPLOAD_FOLDER, filename)
            pdf.save(pdf_path)

            # store in session
            session["pdf_path"] = pdf_path

    # 🔥 Answer only if:
    # - question exists
    # - pdf exists in session
    if question and "pdf_path" in session:
        answer = answer_from_pdf(
            pdf_path=session["pdf_path"],
            question=question,
            api_key=os.getenv("GROQ_API_KEY")
        )

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run()
