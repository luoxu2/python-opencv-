#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/22
#图像直方图（histogram）cmd中pip install matplotlib安装
#实现图像像素直方图的显示
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate ]])
#返回hist
#其中第一个参数必须用方括号括起来。
#第二个参数是用于计算直方图的通道，这里使用灰度图计算直方图，所以就直接使用第一个通道；
#第三个参数是Mask，这里没有使用，所以用None。
#第四个参数是histSize，表示这个直方图分成多少份（即多少个直方柱）。第二个例子将绘出直方图，到时候会清楚一点。
#第五个参数是表示直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素。
#最后是两个可选参数，由于直方图作为函数结果返回了，所以第六个hist就没有意义了（待确定）
#最后一个accumulate是一个布尔值，用来表示直方图是否叠加。


def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    #0——255是图像的range，bins是统计的个数
    #此函数统计像素个数
    #图像像素一般是0-255，习惯上我们喜欢加一位0-256
    plt.show()


def image_hist(image):
    color=('blue','green','red')
    for i,color in enumerate(color):
        #enumerate是枚举
        hist =cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
plot_demo(src)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()