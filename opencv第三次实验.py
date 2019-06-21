#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/13
#用创造一个新图片来探究三通道的不同颜色
import cv2 as cv
import numpy as np
def creat_image():
    img=np.zeros([400,400,3],np.uint8)
    #zeros生成值为零的矩阵数组
    print(img,type(img))
    img[:, :, 2] = np.ones([400, 400]) * 255
    print(img, type(img))
    #img列表的第三个值 0是第一个通道为蓝色，1是第二个通道为绿色，2是第三个通道为红色
    #ones返回一个指定大小和数据类型的矩阵数组
    cv.imshow("new image",img)
    cv.waitKey(0)
creat_image()

a=np.ones([3,3],np.float)
#示例np.ones的用法
a.fill(12.2912323121321)
print(a)
a=np.ones([3,3],np.int)
a.fill(12.212312314)
print(a)
a=a.reshape([1,9])
#改变一个矩阵的形状与值
print(a)