import cv2 as cv
import numpy as np
import random

img = cv.imread("images\\traffic_light.png")

#img = np.empty((500,300,3),np.uint8)
"""
創建一個多維的陣列
(參數1:指定陣列大小及維度->(200:圖高像素,300:圖寬像素,3:有BGR三個值) 
參數2:每一個值的大小，介於0~255之間，所以用.uint8->用二進制表示需要八個位元)
"""

for row in range(100):
    for col in range(img.shape[1]): #得到圖寬
        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        #用 random 隨機產生 BGR 值來創建圖片

cv.imshow('img',img)

cv.waitKey(0)

cv.imwrite('images\\img3.png',img)