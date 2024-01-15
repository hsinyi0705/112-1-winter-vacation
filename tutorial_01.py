import cv2

img = cv2.imread('images\\traffic_light.png') #要讀取的圖片路徑

img = cv2.resize(img, (300,300))
#圖片大小調整，以像素做縮放
#(參數1:想要改變大小的圖片，參數2:想要改成的大小，用像素表示)

cv2.imshow('img',img) 
#圖片顯示，但圖片一顯示出來就會馬上消失
#(參數1:要顯示的視窗，參數2:line3讀入的圖片) 

cv2.waitKey(1000) 
#括號內是圖片停留時間(單位:毫秒，1000毫秒=1秒，0就是一直顯示)