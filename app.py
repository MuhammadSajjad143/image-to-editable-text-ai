import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import easyocr

from llm import format_text_with_llm


@st.cache_resource
def load_easyocr():
    return easyocr.Reader(["en"], gpu=False)


def preprocess_image(image):
    gray = image.convert("L")
    enhanced = ImageEnhance.Contrast(gray).enhance(2)
    sharp = enhanced.filter(ImageFilter.SHARPEN)
    return sharp


def extract_text_easyocr(image):
    reader = load_easyocr()   # SAFE
    image_np = np.array(image)
    results = reader.readtext(image_np)
    return " ".join([res[1] for res in results])


def main():
    st.set_page_config(
        page_title="Image to Editable Text (AI Enhanced)",
        page_icon="📄",
        layout="centered"
    )

    st.title("📸 Image to Editable Text Converter (AI Enhanced)")
    st.write("OCR + optional AI-based formatting (meaning preserved).")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", width=500)

        processed_image = preprocess_image(image)
        st.image(processed_image, caption="Processed Image", width=500)

        if st.button("🔍 Extract Text (OCR Only)"):
            with st.spinner("Extracting text using OCR..."):
                raw_text = extract_text_easyocr(processed_image)

            st.subheader("🧾 OCR Extracted Text")
            st.text_area("OCR Text", raw_text, height=200)

            st.download_button(
                "⬇️ Download OCR Text",
                data=raw_text,
                file_name="ocr_text.txt",
                mime="text/plain"
            )

            st.divider()

            if st.button("✨ Format Text Using AI"):
                with st.spinner("Formatting text using AI..."):
                    clean_text = format_text_with_llm(raw_text)

                st.text_area("AI Formatted Text", clean_text, height=300)

                st.download_button(
                    "⬇️ Download AI Text",
                    data=clean_text,
                    file_name="formatted_text.txt",
                    mime="text/plain"
                )


if __name__ == "__main__":
    main()
