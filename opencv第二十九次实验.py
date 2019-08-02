#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/2
# 视频人脸识别
import cv2 as cv
import numpy as np

def face_dectect_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    face_dectector=cv.CascadeClassifier("D:/opencv-4.0.1-vc14_vc15/opencv/build/etc/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces=face_dectector.detectMultiScale(gray,1.02,5)
    for x,y,w,h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",image)

capture=cv.VideoCapture(0)
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
while(True):
    ret,frame=capture.read()
    frame=cv.flip(frame,1)
    face_dectect_demo(frame)
    c=cv.waitKey(10)
    if c==27:
        break