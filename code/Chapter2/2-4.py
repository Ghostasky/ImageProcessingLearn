import cv2
import numpy as np


img = cv2.imread('Chapter2\\Lena.png')


# jpg 后面那个表示图片质量，越高越好(0-100)
cv2.imwrite('Chapter2\\write1.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite('Chapter2\\write2.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
# png 表示压缩级别
cv2.imwrite('Chapter2\\write3.jpg', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite('Chapter2\\write4.jpg', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
