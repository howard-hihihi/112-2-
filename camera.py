import cv2

# 開啟攝像機（通常camera_index=0表示使用第一個攝像機）
cap = cv2.VideoCapture(0)

# 設定初始視窗大小
cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)

while True:
    # 讀取一幀影像
    '''
    1. ret: 接收 True、False 作為是否讀取成功
    2. frame: 當次讀取的那一偵的圖像, Numpy 數組
    '''
    ret, frame = cap.read()

    # 可以進行額外的處理，例如顯示、保存等
    cv2.imshow('Camera', frame)

    '''
    1. cv2.waitKey(i): i 為等待時間, i=0 為無限期等待, i=1 為等待 0.001 秒
                       , 會讀取鍵盤上的 ASCII, 沒讀取到鍵盤上的東西, 回傳 -1
    2. ord(): 回傳傳入參數的 ASCII, "\x1b" 十六進制
    '''
    if cv2.waitKey(1) == ord("\x1b"):
        print("Close window")
        break
    elif cv2.waitKey(1) == ord("u"):
        print("usseewa")
        

# 釋放攝像機、關閉所有窗口
cap.release()
cv2.destroyAllWindows()
