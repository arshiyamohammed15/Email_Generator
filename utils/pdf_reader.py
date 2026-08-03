"""
Module: pdf_reader.py

Purpose:
Extract plain text from an uploaded PDF resume.

Responsibilities:
- Read uploaded PDF
- Extract text from every page
- Merge extracted text
- Handle invalid or empty PDFs
"""

from PyPDF2 import PdfReader


def extract_text(uploaded_pdf):
    """
    Extract text from an uploaded PDF.

    Args:
        uploaded_pdf: Streamlit UploadedFile object

    Returns:
        str: Extracted resume text

    Raises:
        ValueError: If the PDF is invalid or contains no readable text.
    """

    if uploaded_pdf is None:
        raise ValueError("No PDF file was uploaded.")

    try:
        pdf_reader = PdfReader(uploaded_pdf)

        extracted_pages = []

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_pages.append(page_text.strip())

        resume_text = "\n".join(extracted_pages).strip()

        if not resume_text:
            raise ValueError("The uploaded PDF contains no readable text.")

        return resume_text

    except Exception as error:
        raise ValueError(
            f"Unable to read the uploaded PDF. {error}"
        )