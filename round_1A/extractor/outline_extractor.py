import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
from utils.pdf_utils import guess_title, summarize_text


def extract_text_with_ocr(page):
    pix = page.get_pixmap(dpi=300)
    img_bytes = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_bytes))
    return pytesseract.image_to_string(img)


def extract_outline_and_sections(pdf_path, file_name):
    doc = fitz.open(pdf_path)
    outline = []
    sections = []

    current_section = None
    section_text = ""

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")

        # OCR fallback if no readable text
        if not blocks or all(len(b[4].strip()) == 0 for b in blocks):
            print(f"[OCR] Page {page_num} has no text, using OCR...")
            page_text = extract_text_with_ocr(page)
            blocks = [(0, 0, 0, 0, line.strip()) for line in page_text.splitlines()]
        else:
            blocks = [b for b in blocks if len(b) >= 5 and isinstance(b[4], str)]

        for block in blocks:
            try:
                _, y0, _, _, text, *_ = block
            except ValueError:
                continue

            text = text.strip()

            # Skip images, bullets, or garbage
            if (
                not text or len(text) > 200 or 
                text.startswith("<image") or 
                text.strip() == "•"
            ):
                continue

            words = text.split()

            # Heading detection: position-based
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
