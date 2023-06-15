import os
import synthesis
import generate_pdf
import openai
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return 'index'


@app.route("/synthesis/<path:file_path>", methods=("GET", "POST"))
def get_syntesis(file_path):
    return synthesis.from_pdf_to_syntesis(file_path)


@app.route('/download/')
def download(filepath, name_result):
    return generate_pdf.download_pdf(filepath, name_result)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
