import cv2 as cv

img = cv.imread('images\\i2.jpg')

# 0 - 將圖片放大方便操作
img = cv.resize(img, (0,0), fx=2, fy=2)

imgContour = img.copy() # 複製圖片

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

# 4 - 利用 for 迴圈去跑輪廓
for cnt in contours:
    # 印出輪廓點(這些點連起來就是輪廓)
    print(cnt) 

    # 畫出輪廓
    cv.drawContours(imgContour, cnt, -1, (255,0,0), 4)
    '''
    .drawContours
    (參數1: 要畫在什麼圖形上
    參數2: 要畫的輪廓
    參數3: 要畫第幾個輪廓，-1是指全畫
    參數4: 要用什麼顏色畫
    參數5: 畫的線條粗度)
    '''


cv.imshow('img', img)
cv.imshow('canny', canny)
cv.imshow('imgContour', imgContour)
cv.waitKey(0)

cv.imwrite('images\\img0117-1.png',img)
cv.imwrite('images\\img0117-2.png',canny)
cv.imwrite('images\\img0117-3.png',imgContour)

