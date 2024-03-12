import cv2
import os
from datetime import datetime
from ultralytics import YOLO

# 做好資料管理
DATA_DICT = {"1": {"path": "images/usseewa.jpg", "display": False},
             "2": {"path": "images/mikey.jpeg", "display": False},
             "3": {"path": "images/bon2.png", "display": False},
             "4": {"path": "images/GoingMerry.jpg", "display": False},
             "5": {"path": "images/Sunny.jpg", "display": False},
             "6": {"path": "images/Mashle.jpg", "display": False}}


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

def set_data_all_false(s_dict):
    for key, value in s_dict.items():
        s_dict[key] = False

def save_photo(cap, image_key, kb):
    ret, frame = cap.read()

    # 倒數的數字圖
    one = cv2.imread("images/1.png")
    two = cv2.imread("images/2.png")
    three = cv2.imread("images/3.png")

    new_h, new_w = frame.shape[1]//5, frame.shape[0]//5
    one = cv2.resize(one, (new_w, new_h))
    two = cv2.resize(two, (new_w, new_h))
    three = cv2.resize(three, (new_w, new_h))


    for i in range(151):
        ret, frame = cap.read()

        # 倒數圖片的區域
        roi = frame[10 : new_h + 10, 10 : new_w + 10]

        # 如果 image_key 不是 None 加入圖片的區域
        if image_key is not None:
            frame = show_image(frame, image_key, kb)

        # 使用迴圈模擬倒數，且加入數字圖片
        if i < 50:
            frame[10 : new_h + 10, 10 : new_w + 10] = cv2.addWeighted(roi, 0.3, three, 0.7, 0)
            cv2.waitKey(1)
        elif i < 100:
            frame[10 : new_h + 10, 10 : new_w + 10] = cv2.addWeighted(roi, 0.3, two, 0.7, 0)
            cv2.waitKey(1)
        elif i < 150:
            frame[10 : new_h + 10, 10 : new_w + 10] = cv2.addWeighted(roi, 0.3, one, 0.7, 0)
            cv2.waitKey(1)
        cv2.imshow("Camera", frame)

    # 使用時間當作照片檔名
    now_time = datetime.now()
    time_str = now_time.strftime("%Y-%m-%d %H_%M_%S")
    path = f'photos/{time_str}.jpg'
    os.makedirs("photos", exist_ok=True)
    
    # 儲存照片
    frame[10 : new_h + 10, 10 : new_w + 10] = roi
    cv2.imwrite(path, frame)        

    return frame



if __name__ == "__main__":
    model = YOLO(r'C:\Users\user\Desktop\112-2社課\weights\face_five.pt')
    cls_list = model.names
    switch_dict = {"face": True, "five": False}

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
    
    while True:
        ret, frame = cap.read()
        image_key = None

        # cv2.waitKey() , return type: 'int'
        kb = cv2.waitKey(1)
        if kb == ord("\x1b"): break

        # 預測
        results = model(frame, conf=0.5)
        r = results[0]

        # 繪製預測圖
        annotated_frame = r.plot()


        # 顯示照片
        for data_key, data_info in DATA_DICT.items():
            if kb == ord(data_key) and kb >= ord("1") and kb <= ord("9"):
                print(f'[display {data_info["path"]}]')
                set_data_display(data_key)

            if DATA_DICT[data_key]["display"]:
                image_key = data_key
                annotated_frame = show_image(annotated_frame, data_key, kb)
                
        # 
        for i in range(len(r.boxes.cls)):
            cls = r.boxes.cls[i]
            conf = r.boxes.conf[i]
            if cls_list[int(cls)] == "face" or cls_list[int(cls)] == "five":
                if conf > 0.85:
                    switch_dict[cls_list[int(cls)]] = True

        all_true = all(value for value in switch_dict.values())
        if all_true:
            annotated_frame = save_photo(cap, image_key, kb)

        cv2.imshow("Camera", annotated_frame)
        set_data_all_false(switch_dict)
        

    cap.release()
    cv2.destroyAllWindows()