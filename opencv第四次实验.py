#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/13
#色彩空间
#常见色彩空间有如下几种：
# 1.RGB:RGB颜色空间以R(Red:红)、G(Green:绿)、B(Blue:蓝),俗称三基色模式。
# 2.HSV （Hue, Saturation, Value）主要来捕捉物体的特征颜色用一个inrange就可以表示出来
# 3.HIS(HSI)  [(Hue-Saturation-Intensity(Lightness)]
# 4.YCrCb
# 5.YUV
#inrange函数的基本用法
#1：如果一幅灰度图像的某个像素的灰度值在指定的高、低阈值范围之内，
# 则在dst图像中令该像素值为255，否则令其为0，这样就生成了一幅二值化的输出图像。
#2：每个通道的像素值都必须在规定的阈值范围内！
import cv2 as cv
import numpy as np


def color_space(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
color_space(src)
cv.waitKey(0)
cv.destroyAllWindows()
b,g,r=cv.split(src)
#分离图片的通道函数
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
src2=cv.merge([b,g,r])
cv.imshow("changed src",src)
cv.waitKey(0)
cv.destroyAllWindows()



#一般来说opencv最常见的相互转换有两个
#-hsv与rgb
#-yuv与rgb
