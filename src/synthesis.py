import openai
import parser_1 as parser_1
from flask import render_template
<<<<<<< HEAD:src/synthesis.py
from generate_pdf import download_pdf
from generate_pdf import create_pdf_from_synthesis
=======
import generate_pdf


>>>>>>> a8c13cc60f06c7f36546c537949785f336b58119:synthesis.py


def generate_synthesis(extracted_text):
    prompt = "Can you create a synthesis of the provided text?\nInput: " + \
        extracted_text + "\nSynthesis:"
    synthesis = ""
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None,
    )
    synthesis = response.choices[0].text.strip()
    return synthesis


def extract_name_from_cv(extracted_text):
    prompt = "Extract the name from the given CV:\n" + extracted_text + "\nName:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.3,
        n=1,
        stop=None
    )
    name = response.choices[0].text.strip()
    return name


def display_synthesis(synthesis_result, name):
    return render_template('index.html', text=synthesis_result, name=name)


def from_pdf_to_syntesis(pdf):
    extracted_text = parser_1.parse_pdf(pdf)
    synthesis_result = generate_synthesis(extracted_text)
    name_result = extract_name_from_cv(extracted_text)
    filepath = create_pdf_from_synthesis(synthesis_result, name_result)
    return download_pdf(filepath, name_result)
