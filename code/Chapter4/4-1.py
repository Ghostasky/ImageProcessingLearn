import cv2
import numpy as np

img = cv2.imread('Chapter4\\luo.png')


# 图像各像素加100
m = np.ones(img.shape, dtype="uint8")*100
n = np.zeros(img.shape, dtype="uint8")
print(m)
res = cv2.add(img, m)
res2 = cv2.subtract(m, img)
res3 = cv2.bitwise_and(img, m)
# cv2.imshow("test", img)
# cv2.imshow("winname", res)
# cv2.imshow("13", res2)
cv2.imshow("aa", res3)
cv2.waitKey(0)
cv2.destroyAllWindows()
