#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/2
# 图片中人脸检测
import cv2 as cv
import numpy as np

def face_dectect_demo():
    gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    face_dectector=cv.CascadeClassifier("D:/opencv-4.0.1-vc14_vc15/opencv/build/etc/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces=face_dectector.detectMultiScale(gray,1.02,1)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",src)

src=cv.imread("C:/Users/17913/python+opencv/xiaohai.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
face_dectect_demo()
cv.waitKey(0)
cv.destroyAllWindows()