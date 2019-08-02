#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/7/3
#对于超大的图像做出图像二值化的操作
import cv2 as cv
import tensorflow as tf
import pandas as pd
import numpy as np

def big_image_bindary(image):
    print(image.shape)
    cw=256
    ch=256
    h,w=image.shape[:2]
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,ch):
            roi=gray[row:row+ch,col:cw+col]
            ret,dst=cv.threshold(roi,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
            #dst=cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            #这句与上句一样，都是求图像阈值的一种方法，对于不同的图片效果可能不同
            gray[row:row+ch,col:cw+col]=dst
            print(np.std(dst),np.mean(dst))
    cv.imwrite("D:/result_bindary1.png",gray)
    #因为图像很大，所以一般保存下来查看

def big_image_bindary_2(image):
    #加上对超大图像的二值处理加上空白过滤处理
    print(image.shape)
    cw=256
    ch=256
    h,w=image.shape[:2]
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,ch):
            roi=gray[row:row+ch,col:cw+col]
            print(np.std(roi),np.mean(roi))
            dev=np.std(roi)
            if dev<15:
                gray[row:row+ch,col:cw+col]=255
            else:
                ret,dst=cv.threshold(roi,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
                gray[row:row+ch,col:cw+col]=dst
    cv.imwrite("D:/result_bindary2.png",gray)
    #因为图像很大，所以一般保存下来查看

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
big_image_bindary(src)
big_image_bindary_2(src)
cv.waitKey(0)
cv.destroyAllWindows()