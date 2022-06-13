# ImageProcessLearn



学习图像处理和OpenCV的笔记，



>   [OpenCV中文官方文档](https://woshicver.com/)
>
>   https://opencv.apachecn.org/#/
>
>   https://github.com/makelove/OpenCV-Python-Tutorial







# GUI功能

彩色图像 OpenCV 用的 BGR 模式，但是 Matplotlib 显示用的 RGB 模式。因此如果图像用 OpenCV 加载，则 Matplotlib 中彩色图像将无法正常显示





# 核心操作

## 图像基本操作

img.shape第三个返回值为通道数

```python
img = cv2.imread('data/1.jpg', 0)
print(img.shape)
img = cv2.imread('data/1.jpg')

h, w, c = img.shape
# 高，宽，通道
```

