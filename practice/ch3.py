import cv2 as cv
import numpy as np

img = cv.imread("images\\origin.png")
cv.imshow('img', img)
cv.waitKey(0)

#拆解
b,g,r = cv.split(img)
'''
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
cv.waitKey(0)
'''
cv.imwrite('images\\img_0116_new-bb.png',b)
cv.imwrite('images\\img_0116_new-gg.png',g)
cv.imwrite('images\\img_0116_new-rr.png',r)


#垂直合併
lt = cv.imread("images\\img_0116_new-rr.png")
lb = cv.imread("images\\img_0116_new-bb.png")
rt = cv.imread("images\\img_0116_new-gg.png")
rb = img
stackV1 = np.vstack((lt,lb)) #.vstack() 垂直組合圖片
stackV2 = np.vstack((rt,rb)) 
'''
cv.imshow("stackV1", stackV1)
cv.imshow("stackV2", stackV2)
cv.waitKey(0)
'''
cv.imwrite('images\\img_0116_new-stackV1.png',stackV1)
cv.imwrite('images\\img_0116_new-stackV2.png',stackV2)


#水平合併
l = cv.imread("images\\img_0116_new-stackV1.png")
r = cv.imread("images\\img_0116_new-stackV2.png")
stackH1 = np.hstack((l,r))
cv.imshow("stackH1", stackH1)
cv.waitKey(0)
cv.imwrite('images\\img_0116_new-stackH1.png',stackH1)
