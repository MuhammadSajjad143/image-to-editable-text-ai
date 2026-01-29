# 📸 Image to Editable Text Converter (Vision-Based)

This project is a SaaS-based web application that converts text from images into editable text using a pretrained Vision Transformer model.

Instead of traditional OCR, the system uses Microsoft's TrOCR model, which performs especially well on handwritten academic notes and scanned documents.

---

## 🚀 Features

- Upload handwritten or printed images (JPG / PNG)
- Vision-based text extraction (no classical OCR)
- Preserves original text content
- Editable and downloadable text output
- Deployed as a SaaS application using Streamlit Cloud

---

## 🧠 Model Used

- **Microsoft TrOCR (Vision Transformer)**
- Pretrained handwritten text recognition model from Hugging Face

---

## 🛠️ Tech Stack

- Frontend & Backend: Streamlit
- Vision Model: TrOCR (Hugging Face)
- Language: Python
- Deployment: Streamlit Cloud (SaaS)

---

## 📦 Installation (Local)

```bash
pip install -r requirements.txt
streamlit run app.py
