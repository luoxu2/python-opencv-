#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/2
# 基于距离变换的分水岭算法
# 1.输入图像  2.灰度处理  3.二值化处理  4.距离变换  5.寻找种子  6.生成marker
# 7.分水岭变换  8.输出图像
import cv2 as cv
import numpy as np


def watershed_demo():
    #remove noise if any
    print(src.shape)
    blurred=cv.pyrMeanShiftFiltering(src,10,100)

    #gray\binary image
    gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary_image",binary)

    #morphlogh operation
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mb=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    sure_bg=cv.dilate(mb,kernel,iterations=3)
    cv.imshow("mor_opt",sure_bg)

    #distance transform
    dist=cv.distanceTransform(mb,cv.DIST_L2,3)
    dist_output=cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    #cv.imshow("distance-t",dist_output*50)

    ret,surface=cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    #cv.imshow("surdace_bin",surface)

    surface_fg=np.uint8(surface)
    unknown=cv.subtract(sure_bg,surface_fg)
    ret,markers=cv.connectedComponents(surface_fg)
    print(ret)

    #watershed transform
    markers=markers+1
    markers[unknown==255]=0
    markers=cv.watershed(src,markers=markers)
    src[markers==-1]=[0,0,255]
    cv.imshow("result",src)

src=cv.imread("C:/Users/17913/python+opencv/xiaohai.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
watershed_demo()
cv.waitKey(0)
cv.destroyAllWindows()