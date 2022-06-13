import cv2
import numpy as nmp
size = (2560, 1600)

black = nmp.zeros(size)
print(black[34][56])

cv2.imwrite('data/black.jpg', black)

black[:] = 255

cv2.imwrite('data/white.jpg', black)
