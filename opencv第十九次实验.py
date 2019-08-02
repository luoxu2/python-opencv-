#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/7/4
# canny边缘提取算法
#1高斯模糊—Gaussianblue
#2灰度转换
#3计算梯度-sobel/scharr
#4非最大信号抑制，高低阈值链接
#5高阈值输出二值图像
import cv2 as cv
import tensorflow as tf
import pandas as pd
import numpy as np

def edge_demo(image):
    blurred=cv.GaussianBlur(image,(3,3),0)
    gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # x Grodient
    xgrad=cv.Sobel(gray,cv.CV_16SC1,1,0)
    # y Grodient
    ygrad=cv.Sobel(gray,cv.CV_16SC1,0,1)
    #edge
    edge_output=cv.Canny(xgrad,ygrad,50,150)
    cv.imshow("Canny Edge",edge_output)
    dst=cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow("Color Edge",dst)

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
src2=cv.imread("C:/Users/17913/python+opencv/bad apple(1).jpg")
cv.namedWindow("input image",0)
cv.imshow("input image",src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()