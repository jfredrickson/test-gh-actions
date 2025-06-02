import os
import json
from jsonschema import validate, ValidationError

file_path = os.environ["FILE_PATH"]
schema_path = os.environ["SCHEMA_PATH"]

with open(file_path) as f:
    data = json.load(f)

with open(schema_path) as f:
    schema = json.load(f)

try:
    validate(instance=data, schema=schema)
    print("✅ JSON is valid.")
except ValidationError as e:
    print(f"❌ JSON schema validation error: {e.message}")
    exit(1)
