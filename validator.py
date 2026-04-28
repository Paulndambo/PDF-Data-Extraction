from jsonschema import validate, ValidationError


def validate_schema(data, schema):
    validate(instance=data, schema=schema)


def validate_logic(data):
    if len(data.get("experience", [])) == 0:
        raise ValueError("At least one experience entry is required")

    for exp in data["experience"]:
        if not exp.get("responsibilities"):
            raise ValueError(f"Missing responsibilities for {exp.get('company')}")
