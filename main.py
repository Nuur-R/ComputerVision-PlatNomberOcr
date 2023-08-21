from ocrt import perform_ocrt
from platDetection import plateDetec
import multiprocessing

# membaca text dari dataaa.csv
with open('data.csv', 'r') as f:
    data = f.read()

# multiprocessing untuk menjalaanan dua fungsi sekaligus dari fungsi perform_ocr dan plateDetec
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=perform_ocrt, args=('plate/gambarPlate.jpg',))
    p2 = multiprocessing.Process(target=plateDetec, args=('-',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()