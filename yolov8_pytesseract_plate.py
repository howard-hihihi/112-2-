import cv2 # 影像處理套件
from ultralytics import YOLO # 模型套件
import pytesseract # 讀取圖片文字套件
import easyocr # 讀取圖片文字套件
import re # 處理文字


# # 1. 讀取圖像
# plate_img = cv2.imread("images/TOYOTA.jpg")
# height, width, _ = plate_img.shape # 獲取圖像的寬度和高度


cap = cv2.VideoCapture(0)
while cap.isOpened():

    # 1. 讀取相機照片
    success, plate_img = cap.read()

    # 2. 車牌辨識 @
    model = YOLO("weights/plate.pt")
    results = model(plate_img, conf=0.05)
    res = results[0] # results 裡面放了很多張照片的預測結果，但因為這邊只有一張，所以如果 results[1] 就會出錯

    # 3. 獲取座標(bbox)
    boxes_list = res.boxes 
    print("## boxes_list.xyxy:\n", boxes_list.xyxy)
    print("## boxes_list.xywh:\n", boxes_list.xywh)

    # 4. 將車牌切割出來 --> 5. 辨識車牌號碼 --> # 6. 將辨識的號碼顯示在預測的bbox上面
    bbox_points_list = [] # 儲存座標後面用來顯示框框和文字位置
    crop_plate_list = []
    for box in boxes_list.xyxy:
        x1, y1, x2, y2 = int(box[0].item()), int(box[1].item()), int(box[2].item()), int(box[3].item())
        bbox_points_list.append([x1, y1, x2, y2])
        print("## x1, y1, x2, y2 : ", x1, y1, x2, y2)

        # 切割車牌出來看看
        crop_img = plate_img[y1:y2, x1:x2]
        crop_plate_list.append(crop_img)

        # 辨識切割出來的車牌(這邊測試 pytesseract 好像比較差，但我不想太操我的電腦XD)
        cur_text = pytesseract.image_to_string(crop_img, config='--psm 11')
        cur_text = re.sub(r'[^\w\d]', '', cur_text) # 將不是 w (文字)、 d (數字) 取代成 ""，也就是沒東西

        # 顯示數字、並在原圖畫出框
        text_color = (200, 200, 200) # 文字顏色
        background_color = (210, 0, 111) # 框框顏色

        # 獲取文字尺寸
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        thickness = 2
        (text_width, text_height), baseline = cv2.getTextSize(cur_text, font, font_scale, thickness)

        cv2.rectangle(plate_img, (x1, y1 - text_height - 15), (x1 + text_width, y1 + baseline - 10), background_color, -1)
        cv2.putText(plate_img, cur_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, thickness)
        cv2.rectangle(plate_img, (x1, y1), (x2, y2), background_color, 3) # 框起車牌的 bbox


    # 7. 顯示結果
    cv2.imshow("Plates predict", plate_img)

    # 8. 檢測按鈕跳出迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()