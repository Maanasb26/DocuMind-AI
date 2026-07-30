from flask import Flask, render_template, request, jsonify
from rag.document_processor import DocumentProcessor
from rag.rag_pipeline import RAGPipeline
import os

app = Flask(__name__)

processor = DocumentProcessor()

pipeline = RAGPipeline()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global pipeline

    file = request.files["pdf"]

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    os.makedirs("uploads", exist_ok=True)

    filepath = os.path.join(
        "uploads",
        file.filename
    )

    file.save(filepath)

    chunks = processor.process_pdf(filepath)

    # Reload the retriever so it uses the NEW vector database
    pipeline = RAGPipeline()

    return jsonify({

        "status": "success",

        "chunks": chunks

    })


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data["question"]

    answer = pipeline.ask(question)

    return jsonify({

        "answer": answer

    })


if __name__ == "__main__":
    app.run(debug=True)