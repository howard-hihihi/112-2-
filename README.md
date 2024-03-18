## 1. Real-Time Object Detection
**Real-Time Object Detection** : 通常需在 100ms 以內計算出一次偵測  
* step 1 : 讀取影像將影像輸出到  
* step 2 : 將讀到影像傳送給以訓練好的模型偵測
* step 3 : 輸出偵測到的物件的 bounding box (bbox) 繪製出來

**使用 camera.py 實現**  
* ```model = YOLO(r'C:\Users\user\Desktop\112-2社課\weights\face_five.pt')``` 這邊改成自己的路徑
* ![執行結果]([圖片連結](https://github.com/howard-liang-B/112-2-CYCU-Autocontrol/blob/main/show_results/camera/camera_with_yolo.png)https://github.com/howard-liang-B/112-2-CYCU-Autocontrol/blob/main/show_results/camera/camera_with_yolo.png)
  
