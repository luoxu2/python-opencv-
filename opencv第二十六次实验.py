#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/8/1
# 顶帽和黑帽操作
# 图形形态学梯度
import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst=cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    cimage=np.array(gray.shape,np.uint8)
    cimage=100
    #增加一些亮度，以便观察
    cv.add(dst,cimage)
    cv.imshow("top_hat",dst)


def black_hat_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    dst=cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    cimage=np.array(gray.shape,np.uint8)
    cimage=100
    cv.add(dst,cimage)
    cv.imshow("black_hat",dst)


def hat_binary_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst=cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    cv.imshow("top_hat",dst)

def basic_gradient_demo(image):
    #图像心态学的基本梯度
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
    cv.imshow("basic_gradient", dst)


def gradient_demo(image):
    #图像心态学的外梯度与内梯度
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dm=cv.dilate(image,kernel)
    em=cv.erode(image,kernel)
    dst1=cv.subtract(image,em)
    dst2=cv.subtract(dm,image)
    cv.imshow("internal",dst1)
    cv.imshow("external",dst2)



src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#top_hat_demo(src)
#black_hat_demo(src)
gradient_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()