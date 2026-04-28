# 📄 JSON Schema Driven PDF Extraction

A simple, schema-first backend project that demonstrates how to transform semi-structured PDF documents into validated, structured JSON using JSON Schema.

This project is designed to reflect real-world scenarios where complex documents must be analyzed, modeled, and converted into reliable data for downstream systems.

---

## 🚀 Overview

The pipeline processes a PDF document (CV) and:

1. Extracts raw text
2. Segments the document into logical sections
3. Maps content into a structured JSON model
4. Validates the output using JSON Schema
5. Applies additional logical validation rules

The focus is on **data modeling, schema design, and validation**, not just parsing.

---

## 🧠 What This Demonstrates

* Designing JSON Schema from scratch
* Modeling nested and repeatable data structures
* Handling semi-structured documents
* Defining required vs optional fields
* Applying field-level validation (types, formats, constraints)
* Implementing validation beyond JSON Schema (business rules)
* Translating unstructured input into consistent data contracts

---

## 🏗️ Project Structure

```
.
├── main.py          # Entry point
├── parser.py        # PDF extraction and parsing logic
├── schema.py        # JSON Schema definition
├── validator.py     # Schema + logical validation
├── sample_cv.pdf    # Example input document
└── README.md
```

---

## ⚙️ Installation

```bash
pip install pdfminer.six jsonschema
```

---

## ▶️ Usage

```bash
python main.py sample_cv.pdf
```

---

## 📦 Example Output

```json
{
  "personal_info": {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "phone": "+2547123456789",
    "github": "https://github.com/User-X"
  },
  "experience": [
    {
      "company": "Company X,
      "role": "Software Engineer",
      "responsibilities": [
        "Led backend automation systems",
        "Designed scalable services"
      ]
    }
  ]
}
```

---

## 🧩 Design Approach

### Schema First

The JSON Schema is defined before extraction logic. This establishes a clear data contract and ensures consistent output structure.

### Separation of Concerns

* `parser.py` → handles extraction and transformation
* `schema.py` → defines structure and constraints
* `validator.py` → enforces correctness

### Real-World Focus

The parser is intentionally simple but handles:

* Section-based documents
* Repeated entities (experience entries)
* Inconsistent formatting

---

## ✅ Validation Strategy

### JSON Schema Validation

Ensures:

* Correct structure
* Data types
* Required fields

### Logical Validation

Handles constraints not easily expressed in JSON Schema:

* At least one experience entry must exist
* Each experience must include responsibilities

---

## 📌 Limitations

* Works best with text-based PDFs (no OCR support)
* Parsing relies on simple heuristics and regex
* Not optimized for multiple document formats

---

## 🔮 Possible Improvements

* Support multiple document types (e.g. invoices, bank statements)
* Schema modularization using `$ref`
* Schema versioning
* OCR support for scanned documents
* AI-assisted extraction for complex layouts
* API layer for real-time processing

---

## 🎯 Why This Project

This project highlights core competencies required for a JSON Schema Developer:

* Data modeling and schema design
* Structuring complex, semi-structured inputs
* Embedding validation logic into schemas
* Ensuring data consistency and reliability

---

## 📚 References

* [https://json-schema.org/](https://json-schema.org/)
* [https://python-jsonschema.readthedocs.io/](https://python-jsonschema.readthedocs.io/)
* [https://pdfminersix.readthedocs.io/](https://pdfminersix.readthedocs.io/)

---

## 👤 Author

**Paul Ndambo**
Backend Engineer | Python | Distributed Systems
📍 Nairobi, Kenya
🔗 [https://github.com/Paulndambo](https://github.com/Paulndambo)
