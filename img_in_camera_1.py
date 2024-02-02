import cv2

usseewa = cv2.imread("usseewa.jpg")
cap = cv2.VideoCapture(0)

cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    # 調整 img 大小
    cam_h, cam_w, _ = frame.shape
    img_h, img_w = cam_h//4, cam_w//4
    usseewa = cv2.resize(usseewa, (img_w, img_h))

    # roi(region of interest): img 在 frame 裡面的區域
    roi = frame[cam_h-img_h:cam_h, cam_w-img_w:cam_w]

    # 把 img 加入 frame 裡面
    '''
    dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)
       -src1: 第一個輸入圖像。
       -alpha: 第一個輸入圖像的權重，即合併時的比例。
       -src2: 第二個輸入圖像。
       -beta: 第二個輸入圖像的權重，即合併時的比例。
       -gamma: 一個加到合併結果上的數值。
    '''
    alpha = 0.4
    beta = 1 - alpha
    frame[cam_h-img_h:cam_h, cam_w-img_w:cam_w] = cv2.addWeighted(roi, alpha, usseewa, beta, 0)

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("\x1b"):
        break

cap.release()
cv2.destroyAllWindows()