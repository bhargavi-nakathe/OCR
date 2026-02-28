import streamlit as st
from ocr_engine import extract_word_data
from classifier import classify_receipt
from parser import extract_total, extract_items, reconstruct_lines, lines_to_text

st.title("Receipt OCR & Classification")

uploaded_file = st.file_uploader("Upload Receipt", type=["jpg", "png"])

if uploaded_file is not None:

    # Save file temporarily
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text
    df = extract_word_data("temp.jpg")

    st.subheader("Extracted Items")

    lines = reconstruct_lines(df)
    items = extract_items(lines)
    total = extract_total(lines)

    st.subheader("RAW OCR TEXT DEBUG")
    #st.text(repr(text))
    for item in items:
        st.write(f"{item['name']} - {item['price']}")

    st.subheader("Total")
    st.success(total)

    # Classify
    text = lines_to_text(lines)

    category, confidence = classify_receipt(text)

    st.subheader("Predicted Category")
    st.success(f"{category} ({confidence*100:.2f}% confidence)")