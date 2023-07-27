
from fpdf import FPDF
from flask import send_file

pdf = FPDF()


def create_pdf_from_synthesis(synthesis_result, name_result):
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name_result + synthesis_result,
             ln=1, align='C')
    filepath = pdf.output(f'synthèseCV{name_result}.pdf')
    return filepath


def download_pdf(filepath, name_result):
    filepath = filepath
    name_result = name_result
    return send_file(filepath, mimetype='application/pdf', as_attachment=True, download_name=f'syntesis{name_result}')
