import streamlit as st
from ocr_engine import extract_text
from classifier import classify_receipt
from parser import extract_items_and_total

st.title("Receipt OCR & Classification")

uploaded_file = st.file_uploader("Upload Receipt", type=["jpg", "png"])

if uploaded_file is not None:

    # Save file temporarily
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text
    text = extract_text("temp.jpg")

    items, total = extract_items_and_total(text)

    st.subheader("Extracted Items")

    for item in items:
        st.write(f"{item['name']} - {item['price']}")

    st.subheader("Total")
    st.success(total)

    # Classify
    category, confidence = classify_receipt(text)

    st.subheader("Predicted Category")
    st.success(f"{category} ({confidence*100:.2f}% confidence)")