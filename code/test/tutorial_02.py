import cv2 as cv

cap = cv.VideoCapture(0)
#cv.VideoCapture(index)，index為鏡頭編號，若有其它鏡台才需修改，否則為0

while True:
    ret, frame = cap.read()
    cv.imshow('video', frame)
    if (cv.waitKey(1) == ord('q')): #不斷偵測
        break #按下 q 鍵停止

cap.release() #釋放出鏡頭
cv.destroyAllWindows() #關閉所有視窗