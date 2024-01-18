import cv2 as cv

cap = cv.VideoCapture("images\\f1.mp4") # 讀入影片檔案

while True:
    ret, frame = cap.read()
    '''
    ret: 看影片的下一幀有沒有讀取成功(ture or false)
    frame: 影片的下一幀畫面
    '''

    if ret:
        frame = cv.resize(frame, (0, 0), fx=2, fy=2) # 改變影片視窗大小，做法和改圖片的部分相同
        cv.imshow('video', frame)
    else:
        break

    if (cv.waitKey(3) == ord('q')): # 設定強行終止影片播放按鍵
        break
    

