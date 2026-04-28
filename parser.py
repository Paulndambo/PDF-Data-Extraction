import re
from pdfminer.high_level import extract_text


def extract_text_from_pdf(file_path: str) -> str:
    return extract_text(file_path)


def split_sections(text: str):
    sections = {"header": []}
    current = "header"

    markers = [
        "SUMMARY",
        "TECHNICAL LEADERSHIP SKILLS",
        "PROFESSIONAL EXPERIENCE",
        "EDUCATION"
    ]

    for line in text.splitlines():
        line = line.strip()

        if line in markers:
            current = line.lower().replace(" ", "_")
            sections[current] = []
        else:
            sections[current].append(line)

    return {k: "\n".join(v) for k, v in sections.items()}


def extract_personal_info(header_text: str):
    name_match = re.search(r"^[A-Z\s]+", header_text)
    email_match = re.search(r"\S+@\S+", header_text)
    phone_match = re.search(r"\+?\d[\d\s]{7,}", header_text)
    github_match = re.search(r"https?://github.com/\S+", header_text)

    return {
        "name": name_match.group(0).title() if name_match else "",
        "email": email_match.group(0) if email_match else "",
        "phone": phone_match.group(0) if phone_match else "",
        "github": github_match.group(0) if github_match else ""
    }


def extract_experience(exp_text: str):
    blocks = exp_text.split("\n\n")
    results = []

    for block in blocks:
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        if len(lines) < 2:
            continue

        header = lines[0]
        role = lines[1]

        responsibilities = [
            l.replace("•", "").strip()
            for l in lines[2:]
            if l.startswith("•")
        ]

        results.append({
            "company": header.split("–")[0].strip(),
            "role": role,
            "responsibilities": responsibilities
        })

    return results
