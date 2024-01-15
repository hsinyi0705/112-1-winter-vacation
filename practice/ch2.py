import cv2 as cv
import numpy as np

img = cv.imread("images\\traffic_light.png")

#cv.imshow("img",img)

#cv.waitKey(0)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if ((img[i,j]==[28,217,248]).all()):
            img[i,j] = [255,255,255] #BGR
        #於迴圈中加入判斷式，可以只對符合條件的像素做修改

cv.imshow("img",img)

cv.waitKey(0)

cv.imwrite('images\\ch2.png',img)

