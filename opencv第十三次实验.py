#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/27
# 直方图反向投影(特征颜色捕捉，反向寻找原图的相似颜色)
# 反向投影用于在输入图像（通常较大）中查找特定图像（通常较小或者仅1个像素，以下将其称为模板图像）最匹配的点或者区域，也就是定位模板图像出现在输入图像的位置。
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo(image1,image_little):
    roi_hsv=cv.cvtColor(image_little,cv.COLOR_BGR2HSV)
    target_hcv=cv.cvtColor(image1,cv.COLOR_BGR2HSV)
    cv.imshow("image",image1)
    cv.imshow("image_little",image_little)
    roihist=cv.calcHist([roi_hsv],[0,1],None,[32,32],[0,180,0,256])
    # 加红部分越小，匹配越放松，匹配越全面，若是bsize值越大，则要求得越精细，越不易匹配，所以导致匹配出来的比较小
    cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
    #对直方图做一个规划
    dst=cv.calcBackProject([target_hcv],[0,1],roihist,[0,180,0,256],1)
    # 反向投影函数，它的范围参数与直方图函数一定要是一致的
    cv.imshow("backprojectiondemo",dst)


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv.imshow("hist2d",hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title(">D Histogram")
    plt.show()

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
src1=cv.imread("C:/Users/17913/python+opencv/xuanji.png")
src2=cv.imread("C:/Users/17913/python+opencv/xuanji little.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#cv.imshow("input image",src)
#hist2d_demo(src)
back_projection_demo(src1,src2)
cv.waitKey(0)
cv.destroyAllWindows()