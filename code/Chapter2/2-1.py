import cv2

img = cv2.imread("./Chapter2\\huawei.png")
weith, heigh, c = img.shape
print(weith , heigh, c)
