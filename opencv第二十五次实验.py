#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/1
# 图像形态学的开操作与闭操作
# 开操作与闭操作就是膨胀加腐蚀，输入图像加上结构元素
# 开操作可以去除小的干扰块，闭操作可以填充闭合区域，实现水平或者垂直线提取
import cv2 as cv
import numpy as np

def open_demo(image):
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    #通过修改（x，y）的值，可以提取不同方向的线段与图形
    binary=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open_result",binary)

def close_demo(image):
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    binary=cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("close_result",binary)

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#open_demo(src)
close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()