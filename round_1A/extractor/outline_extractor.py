import fitz
from utils.pdf_utils import guess_title, summarize_text

def extract_outline_and_sections(pdf_path, file_name):
    doc = fitz.open(pdf_path)
    outline = []
    sections = []

    current_section = None
    section_text = ""

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")

        for block in blocks:
            try:
                _, y0, _, _, text, *_ = block
            except ValueError:
                continue

            text = text.strip()

            # Skip invalid blocks
            if (
                not text or len(text) > 200 or 
                text.startswith("<image") or 
                text.strip() == "•"
            ):
                continue

            words = text.split()

            # Detect headings
            if y0 < 200 and len(words) <= 12 and text[0].isupper():
                level = "H1" if len(words) <= 3 else "H2"

                # Save previous section
                if current_section:
                    summary = summarize_text(section_text)
                    sections.append({
                        "title": current_section,
                        "summary": summary
                    })

                # Start new section
                current_section = text
                section_text = ""

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num
                })
            else:
                if not text.startswith("<image") and text != "•":
                    section_text += " " + text

    # Add last section
    if current_section:
        summary = summarize_text(section_text)
        sections.append({
            "title": current_section,
            "summary": summary
        })

    return {
        "title": file_name,
        "outline": outline,
        "sections": sections
    }
