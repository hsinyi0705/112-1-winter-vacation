import cv2 as cv

img = cv.imread("images\\traffic_light.png")

cv.rectangle(img, (90,50), (125,85), (0,0,255), 3) #紅
cv.rectangle(img, (90,92), (125,128), (43,255,253), 3) #黃
cv.rectangle(img, (90,135), (125,170), (0,255,0), 3) #綠
"""
(圖片, (x1,y1):左上座標, (x2,y2):右下座標, (B,G,R), 線粗)
"""

cv.imshow("img", img)

cv.waitKey(0)

cv.imwrite('images\\ch1.png',img)