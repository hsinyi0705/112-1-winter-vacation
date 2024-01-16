import cv2 as cv

img = cv.imread("images\\traffic_light.png")

img = cv.resize(img, (0,0), fx=2, fy=2)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
(要轉換的圖片，COLOR_BGR2GRAY: BGR 轉成 GRAY)
'''

#cv.imshow('img', img)

cv.imshow('gray', gray)

cv.waitKey(0)

cv.imwrite('images\\img_0116.png',gray)