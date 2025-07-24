import os
import json
import ocrmypdf
from extractor.outline_extractor import extract_outline_and_sections

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
TEMP_DIR = "./temp"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(INPUT_DIR, filename)
        temp_ocr_path = os.path.join(TEMP_DIR, f"ocr_{filename}")
        output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

        print(f"🔍 Preprocessing {filename} with OCR...")

        try:
            # Run OCR with Hindi, English, and Japanese
            ocrmypdf.ocr(
                pdf_path,
                temp_ocr_path,
                use_threads=True,
                force_ocr=True,
                language="hin+eng+jpn",
                progress_bar=False
            )
        except Exception as e:
            print(f"⚠ OCR failed for {filename}: {e}")
            temp_ocr_path = pdf_path  # fallback to original file

        print(f"📄 Extracting from: {os.path.basename(temp_ocr_path)}")
        result = extract_outline_and_sections(temp_ocr_path, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"✅ Output saved to {output_path}")

# Clean up temp files (optional)
import shutil
shutil.rmtree(TEMP_DIR)
