import cv2 as cv
import numpy as np

lt = cv.imread("images\\lt.png")
rt = cv.imread("images\\rt.png")
lb = cv.imread("images\\lb.png")
rb = cv.imread("images\\rb.png")

stackV = np.vstack((lt,lb)) #.vstack() 垂直組合圖片
stackH = np.hstack((lt,rt)) #.hstack() 水平組合圖片
'''
待合併的圖片必須是大小完全相同的圖片，且帶入函式時必須用括號框起。
'''

cv.imshow("stackV", stackV)
cv.imshow("stackH", stackH)
cv.waitKey(0)

cv.imwrite('images\\img_0116_new-stackV.png',stackV)
cv.imwrite('images\\img_0116_new-stackH.png',stackH)
