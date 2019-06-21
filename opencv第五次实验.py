#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/16
#实现视频中特征颜色的捕捉
import cv2 as cv
import numpy as np


def vedio_extract():
    capture=cv.VideoCapture("C:/Users/17913/python+opencv/zhonghuazhihuen.mp4")
    while(True):
        ret,frame=capture.read()
        if ret==False:
            break
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv=np.array([37,43,46])
        upper_hsv=np.array([77,255,255])
        success=cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        #这是捕捉视频中的绿色图像，但显示的是白色图像
        #可以将其的白色显示为彩色，有如下方案
        mask=cv.bitwise_and(frame,frame,mask=success)
        cv.imshow("vedio",frame)
        cv.imshow("HSV",success)
        cv.imshow("彩色HSV",mask)
        c=cv.waitKey(30)
        if c==27:
            break
vedio_extract()

