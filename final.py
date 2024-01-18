import cv2 as cv

video = cv.VideoCapture("images\\f1.mp4") # 讀入影片檔案

tracker = cv.TrackerKCF_create() # 初始化追蹤器

# 選擇初始框
ret, frame = video.read() # 讀圖片第一幀
seek = cv.selectROI('cup', video, True, False) # (顯示框名稱，畫在哪，是否在框裡畫十字線，) 


while True:
    ret, frame = video.read()
    '''
    ret: 看影片的下一幀有沒有讀取成功(ture or false)
    frame: 影片的下一幀畫面
    '''

    if ret:
        frame = cv.resize(frame, (0, 0), fx=2, fy=2) # 改變影片視窗大小，做法和改圖片的部分相同
        cv.imshow('video', frame)
    else:
        break
    
    cv.waitKey(5)
    if (cv.waitKey(5) == ord('q')): # 設定強行終止影片播放按鍵 
        break
    

video.release() # 釋放影片和寫入器

cv.destroyAllWindows() # 關閉 OpenCV 窗口
