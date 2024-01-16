import cv2 as cv

img = cv.imread("images\\traffic_light.png")

img = cv.resize(img, (0,0), fx=1.5, fy=1.5)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
'''
BGR 轉 HSV
HSV: 在 HSV 色彩空間下，比BGR 更容易追蹤某種顏色的物體，常用於分割指定顏色的物體。
'''

cv.imshow('img', img)

cv.imshow('hsv', hsv)

cv.waitKey(0)

cv.imwrite('images\\img_0116_original.png',img)
cv.imwrite('images\\img_0116_new.png',hsv)