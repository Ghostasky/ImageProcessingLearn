# ImageProcessLearn



学习图像处理和OpenCV的笔记，



>   [OpenCV中文官方文档](https://woshicver.com/)
>
>   https://opencv.apachecn.org/#/
>
>   https://github.com/makelove/OpenCV-Python-Tutorial





**最终决定看这个吧：**

**https://github.com/eastmountyxz/HWCloudImageRecognition**

[toc]

# 第1篇

图像通常分为二值图像、灰度图像和彩色图像。

-   二值图像：非黑即白，255为白，0为黑（只有这两个
-   灰度图像：RGB(Gray,Gray,Gray)
-   彩色图像：RGB (Red 红色，Green 绿色， Blue 蓝色)

# 第2篇

opencv常见数据类型

-   点Point：`point_list = [(111,111),(222,222)]`
-   颜色Scalar：`(0,0,255)`
-   尺寸Size：`weith, heigh, c = img.shape`

步骤：

1.  读图片
2.  显示
3.  waitkey
4.  destroyAllWindows

## 像素处理

-   灰度图像：返回值 = 图像[位置参数] ，test=img[88,42]
-   彩色图像：返回值 = 图像[位置元素, 0 | 1 | 2 ]获取 BGR 三个通道像 素 

## Numpy像素处理

NumPy 读取像素调用 item()函数实现，修改像素调用 itemset()实现



## opencv创建图像

opencv中没有createimage函数，所以使用numpy库函数实现

调用np.zeros()创建空图

## opencv复制图像

copyImage = img.copy()

## 保存图像

cv2.imwrite("xxxx",img[,])

# 第3篇

画图



# 第4篇

相加，相减，相与或非

# 第5篇

图像融合处理和 ROI 区域绘制

## 图像融合

图像融合通常是指多张图像的信息进行融合，从而获得信息更丰富的结果， 能够帮助人们观察或计算机处理

图像加法：目标图像 = 图像 1 + 图像 2

图像融合：目标图像 = 图像 1 × 系数 1 + 图像 2 × 系数 2 + 亮度调节量

图像融合主要调用 addWeighted()函数实现

## 图像 ROI 区域定位 

ROI（Region of Interest）表示感兴趣区域，是指从被处理图像以方框、 圆形、椭圆、不规则多边形等方式勾勒出需要处理的区域



## 图像属性

shape

size：获取图像的像素数目，其中灰度图像返回行数×列数，彩 色图像返回行数×列数×通道数

dtype：获取图像的数据类型

## 图像通道分离及合并

通过 split()函数和 merge()函数实现对图像通道的处理

## 图像类型转换

在日常生活中，我们看到的大多数彩色图像都是 RGB 类型，但是在图像处 理过程中，常常需要用到灰度图像、二值图像、HSV、HSI 等颜色。图像类型 转换是指将一种类型转换为另一种类型，比如彩色图像转换为灰度图像、BGR 图像转换为 RGB 图像。OpenCV 提供了 200 多种不同类型之间的转换，其 中最常用的包括 3 类，如下：

-   cv2.COLOR_BGR2GRAY
-   cv2.COLOR_BGR2RGB
-   cv2.COLOR_GRAY2BGR

提供了 cvtColor()函数实现这些功能。

