<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/OpenCV_logo_black.svg/180px-OpenCV_logo_black.svg.png" width="200px"></img>
<h2></h2>

<div align="left">

```
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
```

<img src="https://github.com/ultralytics/assets/raw/main/im/banner-ultralytics-github.png" width="1000px"></img>
<h2></h2>
  
```
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
