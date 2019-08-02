#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/7/3
# 图像金字塔，高斯金字塔与拉普拉斯金字塔
# reduce=高斯模糊+降采样（pyrdown），expend=扩大+卷积，还原（prup）
import cv2 as cv
import numpy as np

def pyramid_demoo(image):
    level=3
    temp=image.copy()
    pyramid_images=[]
    for i in range(level):
        dst=cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down"+str(i),dst)
        temp=dst.copy()
    return pyramid_images

def lapalian_demo(image):
    pyramid_images=pyramid_demoo(image)
    level=len(pyramid_images)
    for i in range(level-1,-1,-1):
        if(i-1)<0:
            expand=cv.pyrUp(pyramid_images[i],dstsize=image.shape[:2])
            lpls=cv.subtract(image,expand)
            cv.imshow("laplian_demo_"+str(i),lpls)
        else:
            expand=cv.pyrUp(pyramid_images[i],dstsize=pyramid_images[i-1].shape[:2])
            lpls=cv.subtract(pyramid_images[i-1],expand)
            cv.imshow("lapalian_demo_"+str(i),lpls)

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
src2=cv.imread("C:/Users/17913/python+opencv/xiaohai.jpg")
#cv内的函数不能识别汉字
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#pyramid_demoo(src)
#pyramid_demoo(src2)
#lapalian_demo(src2)
#调用这个函数需要图片是2的n次方才行
cv.waitKey(0)
cv.destroyAllWindows()
