#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/16
#像素运算：算数运算与逻辑运算
#算数运算：可以调节亮度与对比度
#逻辑运算：遮罩层控制
import cv2 as cv
import numpy as np


src1=cv.imread("C:/Users/17913/python+opencv/tangsan1.png")
src2=cv.imread("C:/Users/17913/python+opencv/tangsan2.png")
cv.namedWindow("image1",0)
print(src1.shape)
print(src2.shape)
m1=cv.mean(src1)
#这个函数可以计算图片各像素的均值。
#若均值与方差没有差异则一般情况下可以断定没有加载有用的信息
m2=cv.mean(src2)
print(m1)
print(m2)


m11,dev1=cv.meanStdDev(src1)
m21,dev2=cv.meanStdDev(src2)
print(m11)
print(m21)
print(dev1)
print(dev2)


src3=np.zeros([400,400,3],np.uint8)
cv.imshow("black_floor",src3)
#这里创建了一个黑底，便于进行各种像素运算
m3=cv.mean(src3)
print(m3)
m31,dev3=cv.meanStdDev(src3)
cv.imshow("image1",src1)
cv.imshow("image2",src2)
src4=cv.add(src1,src2)
#像素相加
src5=cv.subtract(src1,src2)
#像素相减
src6=cv.divide(src1,src2)
#像素相除
src7=cv.multiply(src1,src2)
#像素相乘
src8=cv.bitwise_and(src1,src2)
#像素逻辑and运算，对像素进行加和。
src9=cv.bitwise_not(src1)
#像素逻辑not运算,一般用来二通道的黑白图像，将图片黑白互换。
src10=cv.bitwise_or(src1,src2)
#像素逻辑or运算，计算每个位操作分离的两个数组或一个数组和一个标量。
cv.imshow("add_image",src4)
cv.imshow("subtract_image",src5)
cv.imshow("divide_image",src6)
cv.imshow("multiply_image",src7)
cv.imshow("and_image",src8)
cv.imshow("not_image",src9)
cv.imshow("or_image",src10)
cv.waitKey(0)
cv.destroyAllWindows()
