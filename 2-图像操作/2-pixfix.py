import cv2
import numpy as np

img = cv2.imread('data/1.jpg')
h, w, _ = img.shape
px = img[0, 0]
print("0x0: ", px)
print(img[0, 0, 0])

img[0, 0] = [255, 255, 255]
print("0x0: ", img[0, 0])

# 还可以这样修改像素

print(img.item(0, 0, 0))
img.itemset((0, 0, 1), 100)

print(img[0, 0])
