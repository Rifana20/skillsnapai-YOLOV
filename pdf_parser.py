from pdfminer.high_level import extract_text

def extract_pdf_text(file):
    return extract_text(file)

def parse_profile(text):
    lines = text.splitlines()
    headline = lines[0] if lines else ""
    about = "\n".join(lines[1:]).strip()
    return headline.strip(), about.strip()
