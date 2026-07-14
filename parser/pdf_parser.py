import fitz

def extract_text(pdf_input):
    document = fitz.open(stream=pdf_input.read(), filetype="pdf")
    text = ""

    for page in document:
        text += page.get_text()

    return text
