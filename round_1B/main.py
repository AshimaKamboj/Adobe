import os
import json
from extractor.persona_extractor import extract_relevant_sections
from summarizer.persona_summarizer import summarize_for_persona

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate through PDFs in input directory
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".pdf"):
        base_name = filename.rsplit(".", 1)[0]
        pdf_path = os.path.join(INPUT_DIR, filename)
        json_input_path = os.path.join(INPUT_DIR, base_name + ".json")
        json_output_path = os.path.join(OUTPUT_DIR, base_name + ".json")

        # Ensure JSON persona-task exists
        if not os.path.exists(json_input_path):
            print(f"⚠ No corresponding JSON input for {filename}, skipping.")
            continue

        print(f"📄 Processing {filename}...")

        # Load persona & task
        with open(json_input_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)
            persona = metadata.get("persona", "")
            task = metadata.get("task", "")

        # Extract text chunks by importance
        sections = extract_relevant_sections(pdf_path)

        # Generate insights per section
        extracted = []
        for sec in sections:
            summary = summarize_for_persona(sec["text"], persona, task)
            extracted.append({
                "page": sec["page"],
                "heading": sec["heading"],
                "insight": summary
            })

        # Save result
        output = {
            "title": filename,
            "persona": persona,
            "task": task,
            "insights": extracted
        }

        with open(json_output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"✅ Output saved to {json_output_path}")
