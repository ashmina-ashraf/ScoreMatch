import pymupdf4llm
import re


def _convert_pdf_to_markdown(file_path):
    """Convert the PDF content to markdown for the LLM to process it"""

    return pymupdf4llm.to_markdown(file_path)


def _mask_contact_details(text):
    """Remove contact details from the resume"""

    email_pattern = r"([a-zA-Z0-9._-]+)(@[a-zA-Z]+\.[A-Za-z]{2,})"
    updated_text = re.sub(pattern=email_pattern, 
                          repl=r"******\2", 
                          string=text)

    phn_number_pattern = r"(?P<country_code>\+\d{1,3}\s?)?(\d{10})"
    updated_text = re.sub(pattern=phn_number_pattern, 
                          repl=r"\g<country_code>**********", 
                          string=updated_text)

    return updated_text


def _normalize_text(content):
    return content


def read_resume(resume_path):
    resume_content = _convert_pdf_to_markdown(file_path=resume_path)
    masked_resume_content = _mask_contact_details(text=resume_content)
    normalized_resume_content = _normalize_text(masked_resume_content)
    return normalized_resume_content



# --------------- TESTING ---------------------------
if __name__ == "__main__":
    FILE_PATH = r"Resume.pdf"
    content = _convert_pdf_to_markdown(FILE_PATH)
    cleaned = _mask_contact_details(content)
    print(cleaned)