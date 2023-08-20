import easyocr

def perform_ocr(image_path, language='en'):
    # Inisialisasi OCR
    reader = easyocr.Reader([language])
    
    # Gunakan OCR untuk mengenali teks pada gambar
    results = reader.readtext(image_path)
    
    detected_text = []
    for (bbox, text, prob) in results:
        detected_text.append(text)
    
    return detected_text

# # Contoh pemanggilan fungsi
# image_path = 'plat/gambar1.jpg'
# detected_text = perform_ocr(image_path)

# for text in detected_text:
#     print(text)
