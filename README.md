## 1. Real-Time Object Detection
* **Real-Time Object Detection** : 通常需在 100ms 以內計算出一次偵測  
  * step 1 : 讀取影像將影像輸出到  
  * step 2 : 將讀到影像傳送給以訓練好的模型偵測
  * step 3 : 輸出偵測到的物件的 bounding box (bbox) 繪製出來

* **camera.py Flow Chart**  
  <img src="readme images/camera flow chart.png" alt="camera 流程圖" width="80%">  

* **使用 camera.py 實現**  
* ```model = YOLO(r'C:\Users\user\Desktop\112-2社課\weights\face_five.pt')``` 這邊改成自己的路徑
* 執行結果  
  <img src="readme images/camera.png" alt="執行結果" width="50%">  

## 2. 把圖片加入相機中
* **Introduce Variables & Functions**
  * **DATA_DICT** : {"按下的鍵值(ASCII)(key)": {"path": "放入你的影像路徑", "display": False, "type": "image"}, ....}，這個字典儲存了"路徑"、"是否顯示"、"檔案類別"
  * **show_image(cam_frame, image_key, kb)** : 傳入參數有三個，cam_frame 代表相機當下讀取到的那一幀的影像，image_key 代表的是要顯示的影像，對應到我們先前建立的 DATA_DICT 的 key，kb 代表的是當次迴圈讀取到的鍵盤的值，用來檢查是否為 "q" 或 "Esc" 按鍵，"q" 為關閉影像，"Esc" 為跳出迴圈(相機結束讀取)。函式最後會回傳一張加入影像的 frame。
  * **show_video(cap, video, video_key, kb)** : show_image 跟 show_video 差不多，差別是多一個 cap 物件，這個物件是用來讀取相機影像的物件，因為要和影片同時更新，所以我們在 show_video 做更新和顯示影像， show_image 則是回傳後才顯示更新後的影像。
  * **set_data_display(key)** : 這個函式單純就是將我要顯示的影像(照片或影片)的 "display" 的 value 設定成 True，其他的改成 False，就是這麼簡單。

> FPS 由英文 Frames Per Second 縮寫而來，意思是「每秒幀數」。平時我們看的影片其實是由一張張圖片構成，一張就是一幀。當連續播放時，因為「視覺暫留」，看起來就有動態效果。
* **img_video_in_camera.py Flow Chart**  
  <img src="readme images/img_video_in_camera flow chart.png" alt="img_video_in_camera 流程圖" width="100%">  

* 執行結果  
  <img src="readme images/img_video_in_camera.png" alt="執行結果" width="50%">
## 3. Project 1 、 Project 2
* 結合上面兩個做出小專題
* Project 1 : 讀取某特定物體會顯示某特定圖片，例如 : 讀取到 **"face"** 會顯示 **"usseewa.png"**
  * 這邊多了一個函式，**set_data_all_false(s_dict)**，人如其名，就是將所有資料的 display 設定成 False。
  * 
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
