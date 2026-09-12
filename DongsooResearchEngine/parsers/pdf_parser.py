import fitz

def parse_pdf(path):

    doc = fitz.open(path)

    text = []

    for page in doc:
        text.append(
            page.get_text()
        )

    return "\n".join(text)