import cv2 as cv
import numpy as np
import random

hight = 300
width = 300

img = np.zeros((hight,width,3), np.uint8)
'''
[參數1:寬，參數2:為所有，參數3:顏色通道]

陣列元素:
同一參數直接使用 ':' 代表 '到'
單一參數只有 ':' 代表該元素整體
'''
img[0:140, 0:140, 2] = 255 #左上  
img[140:165, 0:140, :] = 255 #左中
img[165:300, 0:140, 0] = 255 #左下

img[0:140, 140:165, :] = 255 #中上
img[140:300, 140:165, :] = 255 #中下

img[0:140, 165:300, 1] = 255 #右上
img[140:165, 165:300, :] = 255 #右中
img[165:300, 165:300, 1] = 255 #右下
img[165:300, 165:300, 2] = 255 #右下

cv.imshow("img",img)
cv.waitKey(0)

cv.imwrite('images\\img_0116_5.png',img)

