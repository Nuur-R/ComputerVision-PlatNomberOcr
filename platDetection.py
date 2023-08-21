import cv2

# Variabel yang akan digunakan untuk deteksi plat nomor
plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

# Membuka akses webcam
cam = cv2.VideoCapture(2)

# Mengatur ukuran window
cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 150)

count = 1
minArea = 500

def plateDetec(plateText):    
    # Membuat perulangan untuk menampilkan webcam
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        # frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        numberPlates = plateCascade .detectMultiScale(frame, 1.1, 4)
        
        for (x, y, w, h) in numberPlates:
            area = w*h
            if area > minArea:
                # Membuat box pada ROI
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                # Menambahkan teks
                cv2.putText(frame,plateText,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
                imgRoi = frame[y:y+h,x:x+w]
                cv2.imwrite("plate/gambarPlate.jpg", imgRoi)
                cv2.imshow("ROI", imgRoi)

        cv2.imshow("Hasil", frame)

        cv2.waitKey(100)
