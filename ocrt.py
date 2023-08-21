import pytesseract
from PIL import Image

def perform_ocrt(image_path, language='eng'):
    # Buka gambar menggunakan PIL
    image = Image.open(image_path)
    
    # Lakukan OCR pada gambar
    detected_text = pytesseract.image_to_string(image, lang=language)
    with open('data.csv', 'w') as f:
            f.write(''.join(detected_text))
    return detected_text

# # Contoh pemanggilan fungsi
# image_path = 'B.jpg'
# detected_text = perform_ocr(image_path)

# print(detected_text)
