import numpy as np

import cv2
img = cv2.imread('data/1.jpg', 0)
print(img.shape)
img = cv2.imread('data/1.jpg')

h, w, c = img.shape
# 高，宽，通道
print(h, w, c)
print(img.dtype)
