#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/20
#实现图像模糊处理(均值模糊，中值模糊，自定义模糊)
#基于离散卷积


import cv2 as cv
import numpy as np


def blur_demo(image):
    #均值模糊
    dst=cv.blur(image,(1,15))
    #图像模糊函数，一般参数采用5*5格式
    #括号内的第一个参数是横向模糊，第二个参数是纵向模糊
    cv.imshow("blur_demo",dst)

def median_blur_demo(image):
    #中值模糊
    dst=cv.medianBlur(image,5)
    cv.imshow(" median_blur_demo",dst)


def custom_blur_demo(image):
    #自定义模糊
    #kernel=np.ones([5,5],np.float32)/25
    #中值模糊
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    #图像的锐化
    dst=cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom_blur_demo",dst)


def gaussian_noise(image):
    #加高斯噪声
    h,w,c=image.shape
    for row in range(h):
        for col in range(w):
            s=np.random.normal(0,200,3)
            #一个正态分布，其特征值是均值与标准差
            b=  image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b+s[0])
            image[row, col, 1] = clamp(g+s[1])
            image[row, col, 2] = clamp(r+s[2])
    cv.imshow("noise image",image)


def clamp(pv):
    if pv>255:
        return 255
    if pv<255:
        return 0
    else :
        return pv


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
gaussian_noise(src)

gs=cv.GaussianBlur(src,(0,0),15)
#高斯模糊，与gaussian_noise可以配合使用
cv.imshow("Gauss_ianBlur",gs)
cv.waitKey(0)
cv.destroyAllWindows()

