#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/7/13
# 实现圆形图形检测
# 1：中值滤波，减少噪声对图像的影响
# 2：检测边缘，发现可能的圆心
# 3：在已有圆心的基础上计算最佳半径
import cv2 as cv
import numpy as np

def detect_circles_demo(image):
    dst=cv.pyrMeanShiftFiltering(image,10,100)
    cimage=cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    circles=cv.HoughCircles(cimage,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(image,(i[0],i[1]),2,(255,0,0),2)
    cv.imshow("circles",image)

src=cv.imread("C:/Users/17913/python+opencv/hough_yuan.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()