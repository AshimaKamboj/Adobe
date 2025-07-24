import fitz  # PyMuPDF
from summarizer.persona_summarizer import summarize_for_persona

def extract_insights(pdf_path, persona_task):
    doc = fitz.open(pdf_path)
    persona = persona_task.get("persona", "general")
    task = persona_task.get("task", "summarize the document")

    page_insights = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if not text.strip():
            continue

        summary = summarize_for_persona(text, persona, task)

        page_insights.append({
            "page": page_num,
            "summary": summary
        })

    result = {
        "title": pdf_path.split("/")[-1],
        "persona": persona,
        "task": task,
        "insights": page_insights
    }

    return result
