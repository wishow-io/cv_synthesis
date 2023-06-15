
import pdfplumber


def parse_pdf(pdf):
    with pdfplumber.open(pdf) as pdf:
        num_pages = len(pdf.pages)

        extracted_text = ""
        for page_number in range(num_pages):
            page = pdf.pages[page_number]
            extracted_text += page.extract_text()
        return extracted_text
