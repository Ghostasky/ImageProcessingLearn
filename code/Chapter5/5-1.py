import cv2
import numpy as np


img1 = cv2.imread('Chapter5\\Lena.png')
img2 = cv2.imread('Chapter5\\luo.png')

res = cv2.addWeighted(img1, 0.6, img2, 0.8, 10)

cv2.imshow("aaaa", res)
print(res.size)
print(res.shape)
print(res.dtype)
cv2.waitKey(0)
cv2.destroyAllWindows()
