import cv2 as cv

img = cv.imread("images\\traffic_light.png")

#常用的 ndarray 屬性

print(f"type{type(img)}")
#資料型態

print(f"size:{img.size}")
#陣列元素個數(長*寬*陣列維度)

print(f"shape:{img.shape}")
#元素個數的位元組，用 resize 可以變更陣列大小

print(f"dim:{img.ndim}")
"""
維度
就看是幾維陣列
"""


"""
result

type<class 'numpy.ndarray'>
size:150984
shape:(233, 216, 3)
dim:3
"""