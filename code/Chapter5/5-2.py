import cv2
import numpy as np


img = cv2.imread('Chapter5\\Lena.png')

b, g, r = cv2.split(img)

# cv2.imshow("winname", b)
# cv2.imshow("winname1", g)
# cv2.imshow("winname2", r)
res = cv2.merge([g, b, r])
res1 = cv2.merge([g, r, b])
res2 = cv2.merge([b, r, g])
cv2.imshow("adf", res)
cv2.imshow("adfa", res1)
cv2.imshow("adsf", res2)
a = cv2.split(img)
print(a)
print(type(a))
cv2.waitKey(0)
cv2.destroyAllWindows()
