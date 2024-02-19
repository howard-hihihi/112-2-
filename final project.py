import cv2
from ultralytics import YOLO

# 做好資料管理
DATA_DICT = {"person": {"path": "images/usseewa.jpg", "type": "image"},
             "cell phone": {"path": "images/mikey.jpeg", "type": "image"},
             "3": {"path": "images/bon2.png", "type": "image"},
             "bottle": {"path": "video/MASHLE op2.mp4", "type": "video"},
             "b": {"path": "video/Gojo field.mp4", "type": "video"}}


def show_image(cam_frame, image_key):
    global DATA_DICT
    
    # 取得照片的 "path"、"display"
    image_info = DATA_DICT.get(image_key)

    # 取得 img , 再調整 img 大小
    image_path = image_info["path"]
    image = cv2.imread(image_path)
    if image is None:
        print("! Read image fail !")
    
    cam_h, cam_w, _ = cam_frame.shape
    img_h, img_w = cam_h // 3, cam_w // 3
    image = cv2.resize(image, (img_w, img_h))

    # roi(region of interest): img 在 frame 裡面的區域
    roi = cam_frame[cam_h - img_h:cam_h, cam_w - img_w:cam_w]

    # img 跟 roi 比例
    alpha = 0.3
    beta = 1 - alpha

    cam_frame[cam_h - img_h:cam_h, cam_w - img_w:cam_w] = cv2.addWeighted(roi, alpha, image, beta, 0)
    return cam_frame

def show_video(cap, model, video_key):
    global DATA_DICT

    video = cv2.VideoCapture(DATA_DICT[video_key]["path"])

    while True:
        cam_ret, cam_frame = cap.read()
        vdo_ret, vdo_frame = video.read()

        # 預測每一帪
        res = model(cam_frame)
        r = res[0]
        annotated_frame = r.plot()

        if cam_ret and vdo_ret:
            # 調整大小
            cam_h, cam_w, _ = cam_frame.shape
            vdo_h, vdo_w = cam_h // 3, cam_w // 3
            vdo_frame = cv2.resize(vdo_frame, (vdo_w, vdo_h))

            # roi
            roi = annotated_frame[cam_h - vdo_h: cam_h, cam_w - vdo_w: cam_w]

            # img 跟 roi 比例
            alpha = 0.3
            beta = 1 - alpha
            
            # roi * alpha + vdo_frame * beta + 0
            annotated_frame[cam_h - vdo_h:cam_h, cam_w - vdo_w:cam_w] = cv2.addWeighted(roi, alpha, 
                                                                                        vdo_frame, beta, 0)
            cv2.imshow("Camera", annotated_frame)
        else:
            annotated_frame[cam_h - vdo_h:cam_h, cam_w - vdo_w:cam_w] = roi
            return annotated_frame
        
        if cv2.waitKey(1) == ord("\x1b") or (len(r.boxes.cls) > 0 and r.boxes.cls[0] == "cat"):
            break


def set_data_display(key):
    global DATA_DICT
    for k in DATA_DICT:
        if k == key:
            DATA_DICT[k]["display"] = True
        else:
            DATA_DICT[k]["display"] = False

def set_all_false():
    global DATA_DICT
    for key in DATA_DICT:
        DATA_DICT[key]["display"] = False

if __name__ == "__main__":
    # 1. 載入模型 
    # 2. 建立相機物件
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # 3. 讀取相機每一帪畫面
        success, frame = cap.read()

        # 4. 預測每一帪
        results = model(frame)
        r = results[0]
        
        # 5. 繪製預測的 bounding box
        annotated_frame = r.plot()

        # 6. 信心值最高的物件、獲取物件的 class name
        best_conf_obj_id = None
        obj_key = None
        if len(r.boxes.cls) > 0:
            best_conf_obj_id = int(r.boxes.cls[0])
            obj_key = r.names[best_conf_obj_id]

        if best_conf_obj_id != None and obj_key in DATA_DICT:
            if DATA_DICT[obj_key]["type"] == "image":
                annotated_frame = show_image(annotated_frame, obj_key)
            elif DATA_DICT[obj_key]["type"] == "video":
                annotated_frame = show_video(cap, model, obj_key)       

        cv2.imshow("Camera", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("\x1b") or obj_key == "cat":
            break


    cap.release()
    cv2.destroyAllWindows()