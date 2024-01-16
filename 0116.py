import cv2 as cv

img = cv.imread("images\\traffic_light.png")

img = cv.resize(img, (0,0), fx=2, fy=2)

canny = cv.Canny(img, 500, 550)
'''
取得圖片的邊緣: 想成描邊的意思比較好理解
(要處理的圖片，最低門檻值:過濾掉，最高門檻值:當邊緣看)
基於像素值差異所造成的效果
在每個像素點打分，和旁邊的像素質差越多分越高
門檻值就是分數
把值放越低輪廓就越明顯
'''

cv.imshow('img', img)

cv.imshow('canny', canny)

cv.waitKey(0)

cv.imwrite('images\\img_0116_original.png',img)
cv.imwrite('images\\img_0116_new.png',canny)