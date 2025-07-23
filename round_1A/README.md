# 🧠 Adobe India Hackathon 2025 — Round 1A: Understand Your Document

This solution extracts a structured outline from any given PDF, including:
- Document Title
- Heading Hierarchy (`H1`, `H2`)
- Section Summaries (auto-generated)

---

## 🚀 Problem Statement

Extract a machine-readable outline from PDFs by identifying headings and organizing document structure in JSON format, without using hardcoded rules or external APIs.

---

## ✅ Features

- 📄 Accepts any PDF from `/app/input`
- 🧩 Extracts:
  - Title
  - Headings (`H1`, `H2`) with page numbers
  - Section summaries (first 1–2 sentences)
- 🧠 Intelligent block parsing (ignores images, bullets, and junk)
- 🔒 Fully offline and stateless
- 🐳 Docker-ready

---

## 🧰 Tech Stack

- Python 3.10+
- [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`) — fast, accurate PDF text extraction
- Regex + heuristics — for heading classification and summary generation

---

## 📦 Installation (Only for local testing)

```bash
pip install -r requirements.txt
python main.py
