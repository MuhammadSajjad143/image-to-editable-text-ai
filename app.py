import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import easyocr

# Cache EasyOCR model (VERY IMPORTANT for performance + deployment)
@st.cache_resource
def load_easyocr():
    return easyocr.Reader(["en"], gpu=False)

def preprocess_image(image):
    """
    Simple preprocessing to improve OCR accuracy
    """
    gray = image.convert("L")
    enhanced = ImageEnhance.Contrast(gray).enhance(2)
    sharp = enhanced.filter(ImageFilter.SHARPEN)
    return sharp

def extract_text_easyocr(image):
    """
    Extract text using EasyOCR
    """
    reader = load_easyocr()
    image_np = np.array(image)
    results = reader.readtext(image_np)
    return " ".join([res[1] for res in results])

def main():
    st.set_page_config(
        page_title="Image to Editable Text",
        page_icon="📄",
        layout="centered"
    )

    st.title("📸 Image to Editable Text Converter")
    st.write(
        "Vision-based text extraction using a pretrained model (EasyOCR). "
        "Extracted text is editable and downloadable."
    )

    uploaded_file = st.file_uploader(
        "Upload an image (JPG, JPEG, PNG)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Original Image", width=500)

        processed_image = preprocess_image(image)
        st.image(processed_image, caption="Processed Image", width=500)

        if st.button("🔍 Extract Text"):
            with st.spinner("Extracting text from image..."):
                extracted_text = extract_text_easyocr(processed_image)

            st.subheader("🧾 Extracted Text (Editable)")
            st.text_area(
                "Text Output",
                extracted_text,
                height=300
            )

            st.download_button(
                label="⬇️ Download Text File",
                data=extracted_text,
                file_name="extracted_text.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
