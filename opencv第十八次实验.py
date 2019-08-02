#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/7/4
# 探究图像梯度
#一阶导数与soble算子
#二阶导数与拉普拉斯算子
import cv2 as cv
import tensorflow as tf
import pandas as pd
import numpy as np #numpy是python的科学记数

def sobel_demo(image):
    grad_x=cv.Sobel(image,cv.CV_32F,1,0)
    #可以将Sobel算子改为Scharr算子，这是一个增强的算子
    grad_y=cv.Sobel(image,cv.CV_32F,0,1)
    gradx=cv.convertScaleAbs(grad_x)
    grady=cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x",gradx)
    cv.imshow("gradient-y",grady)
    gradxy=cv.addWeighted(gradx,0.5,grady,0.5,0)
    #通过addweight函数合并水平方向与竖直方向的边缘图
    cv.imshow("gradient",gradxy)

def lapalian_demo(image):
    #dst=cv.Laplacian(image,cv.CV_32F)
    #lpls=cv.convertScaleAbs(dst)
    #注释部分是原拉普拉斯算子，后为自定义算子
    kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    #拉普拉斯有两个算子，第一个为【0,1,0】，【1，-4,1】，【0,1，0】
    #第二个为【1,1,1,】，【1，-8,1】，【1,1,1】，
    #可以推测出laplacian函数用的第一个，也就是四邻域算子
    #八邻域的算子的效果要强一点
    dst=cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls=cv.convertScaleAbs(dst)
    cv.imshow("lapalain_demo",lpls)


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
#cv内的函数不能识别汉字
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
sobel_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()