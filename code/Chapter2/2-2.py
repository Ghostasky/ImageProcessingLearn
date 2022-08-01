import cv2
import numpy
img = cv2.imread('Chapter2\\Lena.png')


# 区域涂白
# img[100:200, 200:300] = [255, 255, 255]

# cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# numpy 读像素
print(type(img))
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 2))
# 改像素
img.itemset((78, 100, 0), 100)
img.itemset((78, 100, 1), 100)
img.itemset((78, 100, 2), 100)
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 2))

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
