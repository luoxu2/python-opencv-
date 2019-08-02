#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/7/4
#直线检测，霍夫直线变换
import cv2 as cv
import tensorflow as tf
import pandas as pd
import numpy as np

def line_detection(image):
    #如果报错就是没有检测到直线
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,150,apertureSize=3)
    lines=cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        print(type(lines))
        rho,theta=line[0]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b))
        y2=int(y0-1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("image-lines",image)

def line_detct_poossiblecv_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,150,apertureSize=3)
    lines=cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=50,maxLineGap=10)
    for line in lines:
        print(type(line))
        x1,y1,x2,y2=line[0]
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("line_dectect_possible_dedmo",image)


src=cv.imread("C:/Users/17913/python+opencv/line.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
line_detection(src)
line_detct_poossiblecv_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()