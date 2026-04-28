import sys
from parser import extract_text_from_pdf, split_sections, extract_personal_info, extract_experience
from schema import cv_schema
from validator import validate_schema, validate_logic


def process_cv(pdf_path: str):
    text = extract_text_from_pdf(pdf_path)
    sections = split_sections(text)

    data = {
        "personal_info": extract_personal_info(sections.get("header", "")),
        "experience": extract_experience(sections.get("professional_experience", ""))
    }

    # JSON Schema validation
    validate_schema(data, cv_schema)

    # Logical validation
    validate_logic(data)

    return data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <pdf_file>")
        sys.exit(1)

    pdf_file = sys.argv[1]

    try:
        result = process_cv(pdf_file)
        print("Extraction successful:\n")
        print(result)
    except Exception as e:
        print("Error:", str(e))
