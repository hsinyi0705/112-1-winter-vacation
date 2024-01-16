import cv2 as cv

import numpy as np

img = cv.imread("images\\rgb.png")

img = cv.resize(img, (0,0), fx=0.5, fy=0.5)

cv.imshow('img', img)
cv.waitKey(0)

#使用split()拆解色彩通道
b,g,r = cv.split(img)

cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
cv.waitKey(0)

cv.imwrite('images\\img_0116_original.png',img)
cv.imwrite('images\\img_0116_new-b.png',b)
cv.imwrite('images\\img_0116_new-g.png',g)
cv.imwrite('images\\img_0116_new-r.png',r)
