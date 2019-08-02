#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/1
# 基于边缘提取的轮廓发现，分析与查找
import cv2 as cv
import numpy as np

def contours_demo(image):
    dst=cv.GaussianBlur(image,(3,3),0)
    gray=cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    #计算图像梯度，得出阈值
    cv.imshow("binary image",binary)

    contours,sheriachy=cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        #最后一个参数改为-1就会填充轮廓
        print(i)
    cv.imshow("detect contours",image)


src=cv.imread("C:/Users/17913/python+opencv/bianyuan.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
