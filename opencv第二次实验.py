#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/12
#实现视频或摄像头的加载与查看
import cv2 as cv
import numpy as np

def vido_demo():
    capture=cv.VideoCapture("C:/Users/17913/python+opencv/zhonghuazhihuen.mp4")
    #参数为0时，读取摄像头。参数为路径时读取本地视频。
    while(True):
        ret,frame=capture.read()
        #第一个参数ret 为True 或者False,代表有没有读取到图片
        #第二个参数frame表示截取到一帧的图片
        #frame=cv.flip(frame,1)#镜像调换,读摄像头可能需要调换，来符合我们的习惯
        cv.namedWindow("vedio",0)
        cv.imshow("vedio",frame)
        c=cv.waitKey(23)
        if c==27:
            break


vido_demo()
cv.waitKey(0)
cv.destroyAllWindows()