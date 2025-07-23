import os
import json
from extractor.outline_extractor import extract_outline_and_sections

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
        print(f"Processing {filename}...")

        result = extract_outline_and_sections(pdf_path, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"✔ Output saved to {output_path}")
