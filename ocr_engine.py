import pytesseract
import pandas as pd
from preprocess import preprocess_image

def extract_word_data(image_path):

    processed_img = preprocess_image(image_path)

    data = pytesseract.image_to_data(
        processed_img,
        output_type=pytesseract.Output.DATAFRAME,
        config="--oem 3 --psm 4"
    )

    # Remove empty rows
    data = data[data.conf > 40]   # remove low confidence words
    data = data[data.text.notna()]

    return data