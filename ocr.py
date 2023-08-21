import easyocr
import os

def perform_ocr(image_path, language='en'):
    while True:
        # Inisialisasi OCR
        reader = easyocr.Reader([language])
        
        # Gunakan OCR untuk mengenali teks pada gambar
        results = reader.readtext(image_path)
        
        detected_text = []
        for (bbox, text, prob) in results:
            detected_text.append(text)
        
        # Write detected text to data.csv
        with open('data.csv', 'w') as f:
            f.write(''.join(detected_text))
    
# # Contoh pemanggilan fungsi
# image_path = 'OIP.jpeg'
# detected_text = perform_ocr(image_path)
# print(detected_text)
