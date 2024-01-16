import cv2 as cv

img = cv.imread("images\\traffic_light.png")

img = cv.resize(img, (0,0), fx=2, fy=2)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
'''
BGR 轉 RGB
'''

cv.imshow('img', img)

cv.imshow('rgb', rgb)

cv.waitKey(0)

cv.imwrite('images\\img_0116_original.png',img)
cv.imwrite('images\\img_0116_new.png',rgb)