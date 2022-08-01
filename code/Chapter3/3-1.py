import cv2
import numpy as np

# black image
img = np.zeros((256, 256, 3), np.uint8)
for i in range(256):
    img[i] = [255, 255, 255]
# line
cv2.line(img, (0, 0), (100, 256), (55, 255, 155), 1)

# 矩形
cv2.rectangle(img, (50, 50), (100, 100), (255, 0, 0), 1)

# 圆形
cv2.circle(img, (100, 100), 50, (110, 130, 130), 1)
cv2.circle(img, (100, 200), 20, (0, 30, 230), -1)  # 填充

# 椭圆
cv2.ellipse(img, (100, 100), (100, 50), 45, 0, 250, (0, 100, 100))

# 绘制文字
cv2.putText(img, "lalalalala", (200, 100),
            cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 0, 0))
cv2.imshow('winname', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
