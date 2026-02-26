import cv2
import numpy as np

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    # Resize (important for OCR clarity)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # Sharpening
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    sharpen = cv2.filter2D(gray, -1, kernel)

    # Threshold
    _, thresh = cv2.threshold(
        sharpen, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresh