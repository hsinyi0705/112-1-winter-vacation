import cv2 as cv
import numpy as np
import random

hight = 160
width = 280

#以陣列方式建立圖片(灰階)
img1 = np.random.randint(256, size=[hight,width], dtype=np.uint8)
img2 = np.random.randint(256, size=[hight,width,3], dtype=np.uint8)
'''
randint(隨機數最大值，size=[高,寬,維度]，dtype=編碼)

回傳一個以隨機數填滿各元素的的陣列，
維度若不填寫為灰階圖，
填則3為BGR圖
'''

cv.imshow("img1",img1)
cv.imshow("img2",img2)
cv.waitKey(0)

cv.imwrite('images\\img_0116_41.png',img1)
cv.imwrite('images\\img_0116_42.png',img2)
