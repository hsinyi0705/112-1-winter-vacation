import cv2 as cv
import numpy as np
import random

hight = 160
width = 280

#建立BGR圖像(陣列方式)
#先使用zeros建立一全為0的陣列(三通道)，再修改其中欲產生的圖片顏色的通道
img1 = np.zeros((hight,width,3), np.uint8)
img1[:,:,0] = 255 #B通道
img2 = np.zeros((hight,width,3), np.uint8)
img2[:,:,1] = 255 #G通道
img3 = np.zeros((hight,width,3), np.uint8)
img3[:,:,2] = 255 #R通道


cv.imshow("img1",img1)
cv.imshow("img2",img2)
cv.imshow("img3",img3)
cv.waitKey(0)

cv.imwrite('images\\img_0116_431.png',img1)
cv.imwrite('images\\img_0116_432.png',img2)
cv.imwrite('images\\img_0116_433.png',img3)
