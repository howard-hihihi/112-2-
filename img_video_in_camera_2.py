import cv2

# 做好資料管理
DATA_DICT = {"1": {"path": "images/usseewa.jpg", "display": False, "type": "image"},
             "2": {"path": "images/mikey.jpeg", "display": False, "type": "image"},
             "3": {"path": "images/bon2.png", "display": False, "type": "image"},
             "a": {"path": "video/MASHLE op2.mp4", "display": False, "type": "video"},
             "b": {"path": "video/Gojo field.mp4", "display": False, "type": "video"}}


def show_image(cam_frame, image_key, kb):
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
    # cv2.imshow("roi", roi)

    # img 跟 roi 比例
    alpha = 0.3
    beta = 1 - alpha


    # 按下 'q' 關閉照片
    if kb == ord('q'):
        image_info["display"] = False
        cam_frame[cam_h - img_h:cam_h, cam_w - img_w:cam_w] = roi
        print(f"--close {DATA_DICT[image_key]['path']}--")

    cam_frame[cam_h - img_h:cam_h, cam_w - img_w:cam_w] = cv2.addWeighted(roi, alpha, image, beta, 0)
    return cam_frame

def show_video(cap, video, video_key, kb):
    global DATA_DICT

    # 取得影片資訊
    video_info = DATA_DICT.get(video_key)

    while True:
        cam_ret, cam_frame = cap.read()
        vdo_ret, vdo_frame = video.read()
        if vdo_frame is None:
            video_info["display"] = False
            cam_frame[cam_h - vdo_h:cam_h, cam_w - vdo_w:cam_w] = roi
            print(f"--close {DATA_DICT[video_key]['path']}--")
            return cam_frame

        # 再調整大小
        cam_h, cam_w, _ = cam_frame.shape
        vdo_h, vdo_w = cam_h // 3, cam_w // 3
        vdo_frame = cv2.resize(vdo_frame, (vdo_w, vdo_h))

        # roi
        roi = cam_frame[cam_h - vdo_h: cam_h, cam_w - vdo_w: cam_w]
        # cv2.imshow("roi", roi)

        # img 跟 roi 比例
        alpha = 0.3
        beta = 1 - alpha

        # 按下 'q' 關閉照片
        if kb == ord('q'):
            video_info["display"] = False
            cam_frame[cam_h - vdo_h:cam_h, cam_w - vdo_w:cam_w] = roi
            print(f"--close {DATA_DICT[video_key]['path']}--")
            return cam_frame
        
        # roi * alpha + vdo_frame * beta + 0
        cam_frame[cam_h - vdo_h:cam_h, cam_w - vdo_w:cam_w] = cv2.addWeighted(roi, alpha, 
                                                                              vdo_frame, beta, 0)
        cv2.imshow("Camera", cam_frame)
        kb = cv2.waitKey(1)

def set_data_display(key):
    global DATA_DICT
    for k in DATA_DICT:
        if k == key:
            DATA_DICT[k]["display"] = True
        else:
            DATA_DICT[k]["display"] = False



if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
    
    
    while True:
        ret, frame = cap.read()

        # keyboard(kb), return type: 'int'
        kb = cv2.waitKey(1)
        if kb == ord("\x1b"): break
    
        # 把要顯示的圖片 display 變成 true, type(data_key): 'str'
        # 處理後再顯示
        for data_key, data_info in DATA_DICT.items():
            # 設定 True、False
            if kb == ord(data_key) and kb >= ord("1") and kb <= ord("9"):
                print(f'[display {data_info["path"]}]')
                set_data_display(data_key)
            elif kb == ord(data_key) and kb >= ord("a") and kb <= ord("z"):
                print(f'[display {data_info["path"]}]')
                set_data_display(data_key)

            # 顯示 True data
            if DATA_DICT[data_key]["display"] and DATA_DICT[data_key]["type"] == "image":
                frame = show_image(frame, data_key, kb)
            elif DATA_DICT[data_key]["display"] and DATA_DICT[data_key]["type"] == "video":
                video = cv2.VideoCapture(DATA_DICT[data_key]["path"])
                frame = show_video(cap, video, data_key, kb)

        cv2.imshow("Camera", frame)
        

    cap.release()
    cv2.destroyAllWindows()
