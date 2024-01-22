import cv2 as cv
import numpy as np
import random

hight = 150
width = 300

img1 = np.zeros((hight,width,3), np.uint8)
'''
[參數1:寬，參數2:為所有，參數3:顏色通道]

陣列元素:
同一參數直接使用 ':' 代表 '到'
單一參數只有 ':' 代表該元素整體
'''
img1[0:50, :, 0] = 255  
img1[50:100, :, 1] = 255
img1[100:150, :, 2] = 255 


cv.imshow("img1",img1)
cv.waitKey(0)

cv.imwrite('images\\img_0116_431.png',img1)

