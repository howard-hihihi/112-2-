'''
start()	啟用執行緒。
join()	等待執行緒，直到該執行緒完成才會進行後續動作。
'''

import threading
import cv2

def show_usseewa():
    img = cv2.imread("usseewa.jpg")
    cv2.imshow("usseewa", img)
    cv2.waitKey()
    cv2.destroyWindow("usseewa")
    print("--close usseewa--")

def show_mikey():
    img = cv2.imread("mikey.jpeg")
    cv2.imshow("mikey", img)
    cv2.waitKey()
    cv2.destroyWindow("mikey")
    print("--close mikey--")

usseewa_thread = threading.Thread(target=show_usseewa)
mikey_thread = threading.Thread(target=show_mikey)

usseewa_thread.start()
mikey_thread.start()
print("press to close")
usseewa_thread.join()
mikey_thread.join()
usseewa_thread.start()
usseewa_thread.join()