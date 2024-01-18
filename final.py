import cv2 as cv

# 讀入影片檔案
cap = cv.VideoCapture("images\\f1.mp4")

ret, frame = cap.read()
'''
ret: 看影片的下一幀有沒有讀取成功(ture or false)
frame: 影片的下一幀畫面
'''

if ret:
    cv.imshow('video', frame)

cv.waitKey(0)

