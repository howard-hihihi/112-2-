import cv2

# 開啟相機
cap = cv2.VideoCapture(0)

# 影片字典，每個按鍵對應一個影片路徑及顯示狀態
video_dict = {
    "a": {"path": "video/MASHLE op2.mp4", "display": False},
    # "b": {"path": "video_b.mp4", "display": False},
    # "c": {"path": "video_c.mp4", "display": False}
}

# 預設選擇的影片鍵
selected_key = None

while True:
    # 讀取相機畫面
    ret, frame = cap.read()

    # 檢查是否有選擇影片，並顯示該影片
    if selected_key is not None and video_dict[selected_key]["display"]:
        video_path = video_dict[selected_key]["path"]
        video = cv2.VideoCapture(video_path)

        while True:
            ret_video, frame_video = video.read()
            if not ret_video:
                break

            frame_video = cv2.resize(frame_video, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 0.7, frame_video, 0.3, 0)
            cv2.imshow('Camera with Video', result)

            # 檢測按鍵事件
            key = cv2.waitKey(30)
            if key == ord('q'):
                break

        video.release()
        cv2.destroyWindow('Camera with Video')

    else:
        # 顯示相機畫面
        cv2.imshow('Camera', frame)

    # 檢測按鍵事件
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key in [ord(k) for k in video_dict.keys()]:
        # 切換選擇的影片鍵
        selected_key = chr(key)

        # 切換影片顯示狀態
        video_dict[selected_key]["display"] = not video_dict[selected_key]["display"]

# 釋放資源
cap.release()
cv2.destroyAllWindows()
