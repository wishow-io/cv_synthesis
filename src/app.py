import os
import synthesis as synthesis
import openai
from flask import Flask
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()
APP_HOST = os.getenv("HOST")
APP_PORT = os.getenv("PORT")


@app.route("/")
def index():
    return 'index'


@app.route("/synthesis")
def get_syntesis(pdf):
    return synthesis.from_pdf_to_syntesis(pdf)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
