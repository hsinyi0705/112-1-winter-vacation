import cv2 as cv
import numpy as np

hight = 160
width = 280

#以陣列方式建立圖片(灰階)
img = np.ones((hight,width), np.uint8)*255
'''
.ones((高，寬)，編碼)

一般opencv的圖片編碼都為uint8，
ones可以將陣列中所有元素都填入1，
再利用*255，
使圖片為白色。
'''

cv.imshow("img",img)
cv.waitKey(0)

cv.imwrite('images\\img_0116_2.png',img)
