import cv2 as cv

img = cv.imread("images\\traffic_light.png")

img = cv.resize(img, (0,0), fx=2, fy=2)

blur = cv.GaussianBlur(img, (9,9), 10)
'''
高斯模糊
(要轉換的圖片，和: 只能是奇數，標準差)
調整和跟標準差可以影響模糊效果，數字越高越糊
'''

cv.imshow('img', img)

cv.imshow('blur', blur)

cv.waitKey(0)

cv.imwrite('images\\img_0116_original.png',img)
cv.imwrite('images\\img_0116_new.png',blur)