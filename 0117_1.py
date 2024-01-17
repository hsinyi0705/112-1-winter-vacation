import cv2 as cv

img = cv.imread('images\\i2.jpg')

# 0 - 將圖片放大方便操作
img = cv.resize(img, (0,0), fx=2, fy=2)

# 1 - 轉成灰階 (因為在檢測輪廓上不需要用到顏色)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2 - 檢測圖片的邊緣 (依狀況調整參數)
canny = cv.Canny(img, 50, 100)

# 3 - 偵測圖片的輪廓
contours, hierarchy = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE) # (圖片，找外輪廓，不做壓縮)
'''
.findContours
(參數1: 要偵測的圖片
參數2: 要使用的模式，例如找外輪廓、內輪廓，或是內外都要
參數3: 要使用的近似方法，可以壓縮水平或垂直的輪廓點。) 

結果會回傳兩個值
-1 輪廓 
-2 階層 (這邊用不到)
'''





cv.imshow('img', img)
cv.imshow('canny', canny)
cv.waitKey(0)

cv.imwrite('images\\img0117-1.png',img)
cv.imwrite('images\\img0117-2.png',canny)
