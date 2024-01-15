import cv2

img = cv2.imread('images\\traffic_light.png') 

img = cv2.resize(img, (0,0),fx=2,fy=2)
#圖片大小調整，以倍數做縮放
"""
(參數1:想要改變大小的圖片
參數2:
參數3:寬度要調成的倍數
參數4:高度要調成的倍數)
"""

cv2.imshow('img',img) 

cv2.waitKey(0) 