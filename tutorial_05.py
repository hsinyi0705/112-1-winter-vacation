import cv2 as cv
import numpy as np

x = np.array([[1,2,3],[1,2,3]])
#常用的 ndarray 屬性

print(f"type{type(x)}")
#資料型態

print(f"size:{x.size}")
#陣列元素個數(長*寬*陣列維度)

print(f"shape:{x.shape}")
#元素個數的位元組，用 resize 可以變更陣列大小

print(f"dim:{x.ndim}")
"""
維度
就看是幾維陣列
"""


"""
result

type<class 'numpy.ndarray'>
size:6
shape:(2, 3)
dim:2
"""