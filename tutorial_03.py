import cv2 as cv

img = cv.imread("images\\traffic_light.png")

cv.rectangle(img, (20,20), (50,50), (0,255,0), 3)
"""
(圖片, (x1,y1):左上座標, (x2,y2):右下座標, (B,G,R), 線粗)
"""

cv.imshow("img", img)

cv.waitKey(0)