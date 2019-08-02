#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/6/4
# 图像二值化（binary image）及其方法，局部或者全局二值化
#对于提取图片文字的效果很好，可以考虑使用
import cv2 as cv
import numpy as np

def threshold_demo(image):
    #全局阈值
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    #cv.THRESH_OTSU一种得出阈值并以其分割的二值化的方法
    #类似求阈值的方法还有cv.THRESH_TRIANGLE等
    print("thresshold value %s"%ret)
    #同时可以修改第三给参数给图片指定阈值，注意赋值后要改掉后面的求阈值的参数
    cv.imshow("binary1",binary)

def local_threshold(image):
    #局部阈值
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    binary=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    #cv.ADAPTIVE_THRESH_MEAN_C与cv.ADAPTIVE_THRESH_GAUSSIAN_C都是该函数找到局部阈值的一种方法
    #函数中的mocksize是必须为奇数
    #自适应阈值函数
    cv.imshow("binary2",binary)

def custom_threshold(image):
    #用自己求的阈值来分割图像
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    h,w=gray.shape[:2]
    m=np.reshape(gray,[1,w*h])
    mean=m.sum()/(w*h)
    print("mean:",mean)
    ret,binary=cv.threshold(gray,mean,255,cv.THRESH_BINARY)
    cv.imshow("binary3",binary)


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",0)
cv.imshow("input image",src)
threshold_demo(src)
local_threshold(src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
#double cvThreshold( const void* srcarr, void* dstarr, double thresh, double maxval, int type );
# srcarr源数组，dstarr为目标数组，thresh为阈值，maxval为欲设最大值，type为阈值处理的类型，有如下几种：
# CV_THRESH_BINARY，表示dsti=(srci>T)?M:0。
# CV_THRESH_BINARY_INV，表示dsti=(srci>T)?0:M。
# CV_THRESH_TRUNC，表示dsti=(srci>T)?M:srci。
# CV_THRESH_TOZERO_INV，表示dsti=(srci>T)?0:srci。
# CV_THRESH_TOZERO，表示dsti=(srci>T)?srci:0。

