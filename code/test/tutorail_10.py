import cv2 as cv
import numpy as np

img = cv.imread("images\\traffic_light.png")

cv.imshow("img",img)

cv.waitKey(0)

for i in  range(1,100):
    for j in range(1,100):
        img[i,j] = [0,0,0] #BGR
#於迴圈中加入判斷式，可以只對符合條件的像素做修改

cv.imshow("img",img)

cv.waitKey(0)

cv.imwrite('images\\img5.png',img)