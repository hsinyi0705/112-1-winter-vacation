import cv2 as cv
import numpy as np

lower = np.array([200,150,31])
#轉換成 NumPy 陣列範圍稍微變小

upper = np.array([225,190,51])
#轉換成 NumPy 陣列範圍稍微加大

img = cv.imread("images\\traffic_light.png")

mask = cv.inRange(img,lower,upper)
"""
使用 inRange
(圖片，上限，下限)
超出上下限範圍的，圖像值變為0
回傳一圖片(陣列)，內容為圖片中符合上下限之間的像素。

使用 OpenCV 的 inrange() 方法，
可以指定一個色彩的最低數值與最高數值 ( 使用 NumPy 陣列 )，
抓取符合這個色彩範圍內的所有像素成為新影像 ( 範圍外的像素都會被過濾掉 )
"""

output = cv.bitwise_and(img,img, mask=mask)
"""
套用影像遮罩
(圖片1，圖片2，mask=遮罩)
回傳一圖片(陣列)，內容為圖1跟圖2為成員做AND運算，再以遮罩覆蓋。
"""

cv.imshow("output",output)

cv.waitKey(0)