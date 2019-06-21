#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/22
#实现边缘保留滤波（EPF）
#高斯双边，均值迁移等操作
import cv2 as cv
import numpy as np

def bi_demo(image):
    dst=cv.bilateralFilter(image,0,100,15)
    #高斯双边模糊
    #sigmacolor取得大一点，使小的差异模糊掉
    #sigmaspace取得小一点，使空间差异大部分保留
    cv.imshow("bi_demo",dst)

def shift_demo(image):
    #均值模糊
    dst=cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("shift_demo",dst)


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()