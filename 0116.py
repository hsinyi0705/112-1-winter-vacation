import cv2 as cv

import numpy as np

img = cv.imread("images\\rgb.png")

img = cv.resize(img, (0,0), fx=0.5, fy=0.5)

cv.imshow('img', img)
cv.waitKey(0)


b,g,r = cv.split(img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
cv.waitKey(0)

#使用 merge() 合併色彩通道
#merge([藍,綠,紅])，回傳值三色彩通道的圖片
img_merge = cv.merge([b,g,r])
cv.imshow('merge',img_merge)
cv.waitKey(0)

cv.imwrite('images\\img_0116_new.png',img_merge)
