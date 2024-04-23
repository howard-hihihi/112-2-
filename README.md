## 1. Real-Time Object Detection
**Real-Time Object Detection** : 通常需在 100ms 以內計算出一次偵測  
* step 1 : 讀取影像將影像輸出到  
* step 2 : 將讀到影像傳送給以訓練好的模型偵測
* step 3 : 輸出偵測到的物件的 bounding box (bbox) 繪製出來

**camera.py flow chart**  
  <img src="readme images/camera flow chart.png" alt="camera 流程圖" width="50%">  

**使用 camera.py 實現**  
* ```model = YOLO(r'C:\Users\user\Desktop\112-2社課\weights\face_five.pt')``` 這邊改成自己的路徑
* 執行結果  
  <img src="readme images/camera.png" alt="執行結果" width="50%">  

## 2. 把圖片加入相機中
* step 1 : 設定好哪些圖片，和各自的路徑，用鍵盤控制要顯示那些照片和影片
* step 2 : 建立顯示照片跟影像的函式
* step 3 : 讀取相機偵測到的照片，並顯示在螢幕上面
* step 4 : step 3 在讀取照片時，同時讀取鍵盤是否有按下特定按鍵，其中代表了你要加入的圖像或影像
* 執行結果  
  <img src="readme images/img_video_in_camera.png" alt="執行結果" width="50%">
## 3. Project 1 、 Project 2
結合上面兩個做出小專題
* Project 1 : 讀取某特定物體會顯示某特定圖片，例如 : 讀取到 **"face"** 會顯示 **"usseewa.png"**
```
DATA_DICT = {"1": {"path": "images/usseewa.jpg", "display": False, "type": "image"},
             "2": {"path": "images/mikey.jpeg", "display": False, "type": "image"},
             "3": {"path": "images/bon2.png", "display": False, "type": "image"},
             "a": {"path": "video/MASHLE op2.mp4", "display": False, "type": "video"},
             "b": {"path": "video/Gojo field.mp4", "display": False, "type": "video"}}
```
* Project 2 : 相機會讀取人臉，當 **"face"** 和 **"five"** 兩個類別同時被偵測到的時候，螢幕會出現 3 2 1 倒數計時，最後會照相，將結果儲存到資料夾
## Yolov8 Ultralytics
* 官網的詳細說明 : https://docs.ultralytics.com/zh/modes/predict/  
* 這邊有一些範例，因為只使用一些，所以沒有全部的範例
[![open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/15u6zdQotiOYI7t90LqCZCnFxp5YsJ9ty/view?usp=sharing)
