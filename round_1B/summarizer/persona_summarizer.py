import re

def clean_text(text):
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def summarize_for_persona(text, persona, task):
    text = clean_text(text)
    
    # Example keyword filters for common tasks/personas
    persona_keywords = {
        "student": ["introduction", "summary", "definition", "example", "important", "key point"],
        "teacher": ["learning objective", "explain", "concept", "teaching"],
        "researcher": ["data", "study", "analysis", "finding", "evidence", "conclusion"],
        "lawyer": ["section", "clause", "legal", "act", "law", "judgement", "case", "penalty"],
        "finance": ["cost", "profit", "investment", "revenue", "growth", "tax"],
        "healthcare": ["symptom", "diagnosis", "treatment", "medicine", "disease", "clinical"]
    }

    keywords = persona_keywords.get(persona.lower(), []) + task.lower().split()
    summary_sentences = []

    # Split text into sentences and filter by keywords
    sentences = re.split(r'(?<=[.!?]) +', text)
    for sentence in sentences:
        if any(kw.lower() in sentence.lower() for kw in keywords):
            summary_sentences.append(sentence)

    # Fallback: if nothing matched, return first 2 sentences
    if not summary_sentences:
        summary_sentences = sentences[:2]

    summary = " ".join(summary_sentences).strip()
    return summary[:500] + ("..." if len(summary) > 500 else "")
