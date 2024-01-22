import cv2 as cv

video = cv.VideoCapture("images\\f1.mp4") # 讀入影片檔案

tracker = cv.TrackerKCF_create() # 初始化追蹤器

'''選擇初始框'''
# 讀圖片第一幀
ret, frame = video.read() 

# 改變影片視窗大小，做法和改圖片的部分相同
frame = cv.resize(frame, (0, 0), fx=2, fy=2) 

# (顯示框名稱，畫在哪，是否在框裡畫十字線，是否從中心開始選擇) 
# .selectROI 會返回一個元組 -> [min_x(左上x), min_y(左上y), w, h]
seek = cv.selectROI('cup', frame, showCrosshair=True, fromCenter=False) 

# 關閉所有窗口
cv.destroyAllWindows() 

# 使用第一幀和 ROI 初始化追蹤器
tracker.init(frame, seek) 


while True:
    ret, frame = video.read()
    '''
    ret: 看影片的下一幀有沒有讀取成功(true or false)
    frame: 影片的下一幀畫面
    '''

    if (ret == False):
        print("影片讀取失敗")
        break

    frame = cv.resize(frame, (0, 0), fx=2, fy=2) 

    # 更新追蹤器
    # seek 是追蹤器返回的當前位置訊息
    ret, seek = tracker.update(frame) 

    if ret: # 成功追蹤的情況下，將追蹤框畫在當前畫面上
        r1 = (seek[0], seek[1]) # 左上 
        r2 = ((seek[0]+seek[2]), (seek[1]+seek[3])) # 右下
        cv.rectangle(frame, r1, r2, (160, 84, 1), 8)
        # .rectangle (要畫的圖片，方框左上座標，方框右下座標，框線顏色，框線粗細)
    
    else:
        cv.putText(frame, "!!! fail !!!", (100,100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        # .putText (要畫的圖片，要寫的字，字的起始座標，字型，文字大小，字的顏色，文字粗度)
    
    
    cv.imshow('video', frame)
    cv.waitKey(5)
   
    if (cv.waitKey(5) == 27): # 設定強行終止影片播放按鍵 
        break
    

video.release() # 釋放影片和寫入器
cv.destroyAllWindows() # 關閉所有窗口


