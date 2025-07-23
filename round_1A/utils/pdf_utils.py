import fitz
import re

def guess_title(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        blocks = page.get_text("blocks")
        for b in sorted(blocks, key=lambda x: x[1]):
            text = b[4].strip()
            if 5 < len(text) < 100:
                return text
        return "Untitled"
    except:
        return "Untitled"

def summarize_text(text):
    # Clean up unwanted characters
    text = text.replace('\n', ' ')
    text = re.sub(r'•+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # Simple extractive summary
    sentences = re.split(r'(?<=[.!?]) +', text)
    summary = ' '.join(sentences[:2])
    return summary[:300] + ("..." if len(summary) > 300 else "")
