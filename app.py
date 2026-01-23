import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

from llm import format_text_with_llm

# Tesseract path (local)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image):
    gray = image.convert("L")
    enhanced = ImageEnhance.Contrast(gray).enhance(2)
    sharp = enhanced.filter(ImageFilter.SHARPEN)
    return sharp


def extract_text(image):
    config = r"--oem 3 --psm 6"
    return pytesseract.image_to_string(image, config=config)


def inject_css():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        }
        h1, h2, h3 {
            color: #0d47a1;
        }
        textarea {
            border-radius: 10px !important;
        }
        .stButton>button {
            background-color: #1976d2;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="Image to Editable Text",
        page_icon="📄",
        layout="centered"
    )

    inject_css()

    st.title("📸 Image to Editable Text Converter")
    st.write("Step 1: OCR Extraction | Step 2: AI Formatting")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", width=500)

        processed_image = preprocess_image(image)
        st.image(processed_image, caption="Processed Image", width=500)

        # ---------------- OCR ONLY ----------------
        if st.button("🔍 Extract Text (OCR Only)"):
            with st.spinner("Extracting text using OCR..."):
                raw_text = extract_text(processed_image)

            st.subheader("🧾 Extracted OCR Text")
            st.text_area("OCR Text", raw_text, height=200)

            st.download_button(
                "⬇️ Download OCR Text",
                data=raw_text,
                file_name="ocr_text.txt",
                mime="text/plain"
            )

            st.session_state["ocr_text"] = raw_text

        # ---------------- AI FORMATTING ----------------
        if "ocr_text" in st.session_state:
            if st.button("✨ Format Text using AI"):
                with st.spinner("Formatting text using AI (Groq)..."):
                    formatted_text = format_text_with_llm(
                        st.session_state["ocr_text"]
                    )

                st.subheader("✨ AI-Formatted Text")
                st.text_area("Formatted Text", formatted_text, height=300)

                st.download_button(
                    "⬇️ Download AI-Formatted Text",
                    data=formatted_text,
                    file_name="formatted_text.txt",
                    mime="text/plain"
                )


if __name__ == "__main__":
    main()
