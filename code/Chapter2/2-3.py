import cv2
import numpy as np


img = cv2.imread('Chapter2\\Lena.png')

emptyImage = np.zeros(img.shape, np.uint8)
print(img.shape)
cv2.imshow("test", emptyImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
