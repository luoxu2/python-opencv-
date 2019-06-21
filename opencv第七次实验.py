#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/17
import cv2 as cv
import numpy as np
#实现控制图像的对比度与亮度


def contrast_brightness_demo(image,c,b):
    #c代表亮度，b代表对比度
    h,w,ch=image.shape
    blank=np.zeros([h,w,ch],image.dtype)
    dst=cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con-bri-demo",dst)


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
contrast_brightness_demo(src,1,20)
#后面的两个数字参数一个是对比度，一个是亮度
cv.waitKey(0)
cv.destroyAllWindows()
