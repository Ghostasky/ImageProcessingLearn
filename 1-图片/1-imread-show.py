import numpy as np
import cv2

# img = cv2.imread('1GUI/data/1.jpg', cv2.IMREAD_COLOR)

# 灰度
# img = cv2.imread('1GUI/data/1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('1GUI/data/1.jpg', cv2.IMREAD_UNCHANGED)
print(img)
cv2.namedWindow('winname')
cv2.imshow('winname', img)


cv2.imwrite('1GUI/data/save.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
