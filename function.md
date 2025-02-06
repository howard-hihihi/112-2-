<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/OpenCV_logo_black.svg/180px-OpenCV_logo_black.svg.png" width="150px"></img>
<h2></h2>

<div align="left">

```
import cv2
cv2.imshow('ESP32', img)     # (str: 視窗名稱, numpy: 要顯示的影像)
cv2.waitKey(0)               # 等待按鍵輸入，然後回傳ASCII值，delay = 0 = 等待無限毫秒
cv2.destroyAllWindows()      # 關閉所有 OpenCV 視窗。
cv2.putText(img, text, org, fontFace, fontScale, color, thickness)     # 將文字放到影像上
  - img：要繪製文字的影像。
  - text：要顯示的文字（str）。
  - org：文字起始座標，(x, y)，左上角為原點。
  - fontFace：字型，cv2.FONT_HERSHEY_PLAIN、cv2.FONT_HERSHEY_DUPLEX。
  - fontScale：字體大小（float）。
  - color：文字顏色，(B, G, R)。
  - thickness：字體粗細（int）。
cv2.rectangle(img, (x1, y1), (x2, y2), color=color, thickness)
  - img：要繪製的影像。
  - (x1, y1)：矩形的左上角座標。
  - (x2, y2)：矩形的右下角座標。
  - color：矩形的顏色（BGR 格式，如 (255, 0, 0) 代表藍色）。
  - thickness：邊框厚度（-1 表示填滿）。
```

<div align="center">
<img src="https://github.com/ultralytics/assets/raw/main/im/banner-ultralytics-github.png" width="800px"></img>
<h2></h2>
<div align="left">
    
```
from ultralytics import YOLO
model = YOLO("yolo11n.pt")          # 載入模型
results = model(source)             # 進行推理
```
### source 可傳入的方式
| source | Example | Type |
|:--     |:--:     |:--:  |
| image	| 'image.jpg' |	str or Path |
| URL	| 'https://ultralytics.com/images/bus.jpg' | str |
| PIL	| Image.open('image.jpg') |	PIL.Image |
| OpenCV	| cv2.imread('image.jpg') | np.ndarray |
| numpy	| np.zeros((640,1280,3)) |	np.ndarray |  
| YouTube	| 'https://youtu.be/LNwODJXcvt4' | str |  	

```
# 因為只傳入一幀影像，也就是只有一張影像被傳入，所以輸出也只有一張影像的預測結果
# 若是傳入3張影像，len(results) = 3
r = results[0]           # 這邊取唯一的那一張的預測結果
coord = r.boxes.xyxy     # 獲取左上和右下的座標 ⚡
coord = r.boxes.xywh     # 獲取左上座標、寬度和長度 ⚡
conf = r.boxes.conf      # 獲取框框(bounding box, bbox)的信心值 ⚡
cls = r.boxes.cls        # 獲取預測到的類別 ⚡
```
以上四個 ```⚡``` 回傳的資料形式都是 list，也就是影像內被預測到的所有物件，假如影像內有三個物件被偵測到，那 len(conf) 就會是 3。

<div align="center">
<img src="https://github.com/urllib3/urllib3/raw/main/docs/_static/banner_github.svg" width="500px"></img>
<h2></h2>

<div align="left">

```
import urllib.request
url = "https://new.ntpu.edu.tw/"         # 設定要請求的網址
response = urllib.request.urlopen(url)   # 發送 HTTP 請求並取得伺服器的回應
print(response.read())                   # 讀取並輸出該網頁的 HTML 原始碼（以 bytes 形式呈現）
```

### 從 URL 讀取圖片，轉換為 NumPy 陣列，並用 OpenCV 解碼為可顯示的影像。
```
imgResponse = urllib.request.urlopen (url)                        
imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)    # np.array必須傳入可迭代的物件，所以須將 bytes轉乘bytearray
img = cv2.imdecode (imgNp,-1)                                     # 將二進制格式的圖片轉換成 OpenCV 可用的物件
```
