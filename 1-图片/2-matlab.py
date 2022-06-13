import numpy as nm
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/1.jpg')
plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # 隐藏 X 和 Y 轴的刻度值

plt.show()
