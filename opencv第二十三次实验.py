#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/1
# 对象检测
# 计算弧长与面积（像素单位）
# 多边形拟合以及几何矩的计算（原点矩，中心矩）
import cv2 as cv
import numpy as np

def measure_object(image):
    #无多边形逼近的几何矩计算
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshold value : %s"%ret)
    cv.imshow("binary image",binary)
    contours,hireachy=cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area=cv.contourArea(contour)
        x,y,w,h=cv.boundingRect(contour)
        mm=cv.moments(contour)
        type(mm)
        cx=mm["m10"]/mm["m00"]
        cy=mm["m01"]/mm["m00"]
        cv.circle(image,(np.int(cx),np.int(cy)),2,(0,255,255),-1)
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        print("contour area %s"%area)
    cv.imshow("measure_contours",image)



def measure_object_gai(image):
    #加入多边形逼近的几何矩计算
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshold value : %s"%ret)
    cv.imshow("binary image",binary)
    dst=cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    contours,hireachy=cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area=cv.contourArea(contour)
        x,y,w,h=cv.boundingRect(contour)
        rate=min(w,h)/max(w,h)
        print("rectangle rate:%s"%rate)
        mm=cv.moments(contour)
        print(type(mm))
        cx=mm["m10"]/mm["m00"]
        cy=mm["m01"]/mm["m00"]
        cv.circle(dst,(np.int(cx),np.int(cy)),2,(0,255,255),-1)
        #cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2)
        print("contour area %s"%area)
        approxcure=cv.approxPolyDP(contour,4,True)
        print(approxcure.shape)
        if approxcure.shape[0]>6:
            cv.drawContours(dst,contours,i,(0,255,0),2)
        if approxcure.shape[0]==4:
            cv.drawContours(dst,contours,i,(0,0,255),2)
        if approxcure.shape[0]==3:
            cv.drawContours(dst,contours,i,(255,0,0),2)
    cv.imshow("measure_contours",dst)


src=cv.imread("C:/Users/17913/python+opencv/num.png")
src2=cv.imread("C:/Users/17913/python+opencv/jihe.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#measure_object(src)
measure_object_gai(src2)
cv.waitKey(0)
cv.destroyAllWindows()