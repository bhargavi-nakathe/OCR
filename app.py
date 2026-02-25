import streamlit as st
from ocr_engine import extract_text
from classifier import classify_receipt

st.title("Receipt OCR & Classification")

uploaded_file = st.file_uploader("Upload Receipt", type=["jpg", "png"])

if uploaded_file is not None:

    # Save file temporarily
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text
    text = extract_text("temp.jpg")

    st.subheader("Extracted Text")
    st.write(text)

    # Classify
    category, confidence = classify_receipt(text)

    st.subheader("Predicted Category")
    st.success(f"{category} ({confidence*100:.2f}% confidence)")