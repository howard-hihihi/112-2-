from ultralytics import YOLO
import cv2

if __name__ == "__main__":
    # 1. 建立相機物件，提供後續的函式
    cap = cv2.VideoCapture(0)

    # 2. 載入模型 
    model = YOLO(r'weights\plate.pt')
    
    # 當cap有讀取相機就回傳 True
    while cap.isOpened():

        # 3. 第一個回傳值是是否讀取成功，第二個回傳值讀取的那一帪畫面
        success, frame = cap.read()

        # 4. 進行車牌的辨識、並獲取每一個物件的座標
        results = model(frame)

        # 5. 

        cv2.imshow("Camera", results[0].plot())
        if cv2.waitKey(1):
            break

    cap.release()
    cv2.destroyAllWindows()