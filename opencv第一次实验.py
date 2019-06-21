#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/11
# #实现图片的打开与查看
import cv2 as cv
import tensorflow as tf
import pandas as pd
import numpy as np #numpy是python的科学记数

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
#cv内的函数不能识别汉字
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
t1=cv.getTickCount()
#此函数计算此程序运行的时间
print(t1)
img=cv.bitwise_not(src)
#将图片改为灰度图像
t2=cv.getTickCount()
print(t2)
print(t2-t1)
cv.imshow("input image2",img)
cv.waitKey(0)
cv.destroyAllWindows()
print(type(src))
print(src.shape)#分辨率(长:height，宽:width)，通道(channels),打印也是对应的顺序
print(src.size)#大小，shape中的长宽高之积就是这个值
print(src.dtype)#每个通道所占的位数，uint8无符号的八位，一个字节
print("hello opencv！")


#gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
#改变图像的颜色通道。
#BGR是色彩数据模式：BGR，灰色数据模式：GRAY
#读取灰度图像
#cv.imwrite("D:/image.jpg",gray)
#图片保存