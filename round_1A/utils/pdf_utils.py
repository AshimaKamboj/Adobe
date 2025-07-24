# import fitz  # PyMuPDF
import re


def guess_title(pdf_path):
    """
    Guess the title from the first page of the PDF.
    """
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        blocks = page.get_text("blocks")

        # Sort by vertical position (top to bottom)
        for b in sorted(blocks, key=lambda x: x[1]):
            if len(b) >= 5:
                text = b[4].strip()
                if 5 < len(text) < 100 and not text.startswith("<image"):
                    return text
        return "Untitled"
    except Exception as e:
        return "Untitled"


def summarize_text(text, max_sentences=2, max_chars=300):
    """
    Clean text and return the first few sentences as a summary.
    """
    # Clean formatting artifacts
    text = re.sub(r'•+', '', text)
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text).strip()

    # Extract first N sentences
    sentences = re.split(r'(?<=[.!?।]) +', text)  # support Hindi (।)
    summary = ' '.join(sentences[:max_sentences])
    summary = summary.strip()

    # Limit to max_chars
    if len(summary) > max_chars:
        summary = summary[:max_chars].rstrip() + "..."

    return summary if summary else "No meaningful content found."
