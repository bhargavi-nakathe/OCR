import pytesseract
from preprocess import preprocess_image

def extract_text(image_path):
    processed_img = preprocess_image(image_path)
    raw_text = pytesseract.image_to_string(processed_img)
    return clean_text(raw_text)

import re

def clean_text(text):
    text = re.sub(r"[^A-Za-z0-9\s.%$]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()