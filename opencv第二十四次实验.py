#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/1
# 图像形态学的膨胀与腐蚀
import cv2 as cv
import numpy as np


def erode_demo(image):
    #腐蚀
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    #后面的（5，5）是腐蚀的程度
    dst=cv.erode(binary,kernel)
    cv.imshow("erode_demo",dst)

def dilate_demo(image):
    #膨胀
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    #后面的（5，5）是膨胀的程度
    dst=cv.dilate(binary,kernel)
    cv.imshow("dilate_demo",dst)

src=cv.imread("C:/Users/17913/python+opencv/1,2.png")
src2=cv.imread("C:/Users/17913/python+opencv/xiaohai.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#erode_demo(src)
#dilate_demo(src)
#kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
#dst=cv.erode(src2,kernel)
#cv.imshow("result",dst)
#彩色图像直接调用函数即可
cv.waitKey(0)
cv.destroyAllWindows()