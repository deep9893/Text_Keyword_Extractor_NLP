import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""  # to save the extracted text

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)  # Load each page
            text += page.get_text()

        pdf_document.close()  # Close the document after extracting text
        return text
    except Exception as e:
        return str(e)
