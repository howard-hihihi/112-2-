import cv2
import os
from ultralytics import YOLO

# 做好資料管理
DATA_DICT = {"1": {"path": "images/usseewa.jpg", "display": False},
             "2": {"path": "images/mikey.jpeg", "display": False},
             "3": {"path": "images/bon2.png", "display": False},
             "4": {"path": "images/GoingMerry.jpg", "display": False},
             "5": {"path": "images/Sunny.jpg", "display": False},
             "6": {"path": "images/lufy_5gear.jpg", "display": False}}


def show_image(cam_frame, image_key, kb):
    global DATA_DICT
    
    # 取得照片的 "path"、"display"
    image_info = DATA_DICT.get(image_key) # 若是 image_key 不存在，會回傳 None

    # 取得 img
    image_path = image_info["path"]
    image = cv2.imread(image_path)
    if image is None:
        print("! Read image fail !")
    
    # 調整大小
    cam_h, cam_w, channel = cam_frame.shape
    img_h, img_w, channel = image.shape
    new_img_w = cam_w // 3
    new_img_h = img_h * new_img_w // img_w
    image = cv2.resize(image, (new_img_w, new_img_h))

    # roi(region of interest): img 在 frame 裡面的區域
    roi = cam_frame[cam_h - new_img_h:cam_h, cam_w - new_img_w:cam_w]
    # cv2.imshow("roi", roi)

    # img 跟 roi 比例
    alpha = 0.3
    beta = 1 - alpha

    # 按下 'q' 關閉照片
    if kb == ord('q'):
        image_info["display"] = False
        cam_frame[cam_h - new_img_h:cam_h, cam_w - new_img_w:cam_w] = roi
        print(f"--close {DATA_DICT[image_key]['path']}--")

    cam_frame[cam_h - new_img_h:cam_h, cam_w - new_img_w:cam_w] = cv2.addWeighted(roi, alpha, image, beta, 0)
    return cam_frame

def set_data_display(key):
    global DATA_DICT
    for k in DATA_DICT:
        if k == key:
            DATA_DICT[k]["display"] = True
        else:
            DATA_DICT[k]["display"] = False

def save_photo(cap, image):
    ret, frame = cap.read()
    one = cv2.imread("images/1.png")
    two = cv2.imread("images/2.png")
    three = cv2.imread("images/3.png")

    new_h, new_w = frame.shape[1]//5, frame.shape[0]//5
    one = cv2.resize(one, (new_w, new_h))
    two = cv2.resize(two, (new_w, new_h))
    three = cv2.resize(three, (new_w, new_h))

    for i in range(270):
        ret, frame = cap.read()
        if i < 50:
            cv2.imshow("Count", three)
            cv2.waitKey(1)
        elif i < 100:
            cv2.imshow("Count", two)
            cv2.waitKey(1)
        elif i < 150:
            cv2.imshow("Count", one)
            cv2.waitKey(1)
        cv2.imshow("Camera", frame)

    cv2.destroyWindow("Count")

    # 避免 photo 名稱重複
    j = 1
    path = f'photos/{str(j)}.jpg'
    while os.path.exists(path):
        j += 1
        path = f'photos/{str(j)}.jpg'
    
    # 儲存照片
    cv2.imwrite(path, frame)        

    return frame



if __name__ == "__main__":
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
    
    
    while True:
        ret, frame = cap.read()

        # cv2.waitKey() , return type: 'int'
        kb = cv2.waitKey(1)
        if kb == ord("\x1b"): break

        # 預測
        results = model(frame)
        r = results[0]

        # 繪製預測圖
        annotated_frame = r.plot()


        # 顯示照片
        for data_key, data_info in DATA_DICT.items():
            if kb == ord(data_key) and kb >= ord("1") and kb <= ord("9"):
                print(f'[display {data_info["path"]}]')
                set_data_display(data_key)

            if DATA_DICT[data_key]["display"]:
                annotated_frame = show_image(annotated_frame, data_key, kb)

        # 67 cell phone
        for idx in r.boxes.cls:
            if idx == 67:
                annotated_frame = save_photo(cap, annotated_frame)

        cv2.imshow("Camera", annotated_frame)
        

    cap.release()
    cv2.destroyAllWindows()