import cv2
import pytesseract

class PlateDetector:
    def __init__(self, cascade_path):
        self.plate_cascade = cv2.CascadeClassifier(cascade_path)
    
    def detect_plates(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plates = self.plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
        return plates
    
    def draw_plates(self, frame, plates):
        for (x, y, w, h) in plates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

def recognize_text(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detected_text = pytesseract.image_to_string(gray_image, lang='eng')
    return detected_text

# Buka video dari webcam
cap = cv2.VideoCapture(2)

# Inisialisasi kelas
plate_detector = PlateDetector('haarcascade_russian_plate_number.xml')

while True:
    ret, frame = cap.read()  # Baca frame dari webcam
    if not ret:
        break
    
    plates = plate_detector.detect_plates(frame)
    plate_detector.draw_plates(frame, plates)
    
    for (x, y, w, h) in plates:
        plate_img = frame[y:y+h, x:x+w]
        detected_text = recognize_text(plate_img)
        
        if detected_text.strip():
            cv2.putText(frame, detected_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'Undetected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow('Plate Detection', frame)
    
    # Tekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
