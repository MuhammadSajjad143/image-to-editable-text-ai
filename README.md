📸 Image to Editable Text (Vision-Based OCR)

This project is a SaaS-based web application that converts text from images into editable and downloadable text using a pretrained vision-based text recognition model.

The application is built with Streamlit and deployed on a SaaS platform (Streamlit Cloud). It allows users to upload an image containing text and extract the text exactly as it appears in the image, without rewriting or altering the content.

🚀 Features

📷 Upload images containing text (JPG / PNG)

🔍 Extract text using a pretrained vision-based OCR model (EasyOCR)

🧾 View extracted text in editable form

⬇️ Download extracted text as a .txt file

☁️ Deployed as a SaaS web application using Streamlit Cloud

⚡ No system-level dependencies (cloud-safe)

🧠 How It Works

User uploads an image containing text

Image is lightly preprocessed to improve recognition accuracy

A pretrained vision-based OCR model extracts text directly from the image

The extracted text:

Matches the content of the image

Is editable inside the app

Can be downloaded as a text file

❗ The system does not paraphrase, summarize, or modify the text in any way.

🛠️ Tech Stack

Frontend & Backend: Streamlit

Text Recognition Model: EasyOCR (Pretrained Vision Model)

Programming Language: Python

Libraries: EasyOCR, Torch, Pillow, NumPy

Deployment Platform: Streamlit Cloud (SaaS)

🎓 Academic Compliance

This project complies with the academic requirement that:

Text must be extracted exactly as present in the image

No AI-based rewriting or semantic alteration is performed

Pretrained vision models are allowed

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py