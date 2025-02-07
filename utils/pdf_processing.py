import pdfplumber

def extract_text_from_pdf(uploaded_file):
    """Mengekstrak teks dari file PDF menggunakan pdfplumber"""
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()
