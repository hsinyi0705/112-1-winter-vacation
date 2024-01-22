import cv2

img = cv2.imread('images\\traffic_light.png') 

img = cv2.resize(img, (0,0),fx=2,fy=2)

cv2.imshow('img',img) 

cv2.waitKey(0) 

cv2.imwrite('images\\img2.png',img)
"""
儲存圖片
("要存到的路徑檔名"，圖片)
"""