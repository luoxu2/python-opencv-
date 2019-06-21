#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/20
#ROI（Region of interest）区域，感兴趣区域,主要用numpy来获取
#实现泛洪填充（也叫漫水填充）

import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyimg=image.copy()
    #复制一张图片
    h,w=image.shape[:2]
    mask=np.zeros([h+2,w+2],np.uint8)
    #这个掩膜mask，就是用于进一步控制哪些区域将被填充颜色
    #它应该为单通道、8位、长和宽上都比输入图像 image 大两个像素点的图像
    cv.floodFill(copyimg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    #漫水填充，第一个是填充图片，后面是遮盖层
    #漫水填充（100，100，100）是最低像素，后面的是增长像素
    cv.imshow("fill_color_demo",copyimg)
    cv.waitKey(0)


def fill_binary():
    image=np.zeros([400,400,3],np.uint8)
    image[100:300,100:300, : ]=255
    cv.imshow("fill_binary",image)
    cv.waitKey(0)
    mask=np.ones([402,402,1],np.uint8)
    mask[101:301,100:301]=0
    #这个ROI是选定的图片中心区域
    cv.floodFill(image,mask,(200,200),(100,2,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("flled_binary",image)
    cv.waitKey(0)

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
face=src[30:350,250:550]
#锁定face这个ROI区域，第一个对应的长度方向，第二个是对应的宽度方向
gray=cv.cvtColor(face,cv.COLOR_BGR2GRAY)
black=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
#将双通道的图片改为三通道的，画都样子没有变，但是通道变了
#不同通道数目的图片是不能使用“=”号的
cv.imshow("face",gray)
src[30:350,250:550]=black
cv.imshow("input image 2",src)
cv.waitKey(0)
cv.destroyAllWindows()
fill_color_demo(src)
fill_binary()




#漫水函数参数详解
#image 【输入/输出】 1或者3通道、 8bit或者浮点图像。仅当参数flags的FLOODFILL_MASK_ONLY标志位被设置时image不会被修改，否则会被修改。
#mask 【输入/输出】 操作掩码，必须为单通道、8bit，且比image宽2个像素、高2个像素。使用前必须先初始化。Flood-filling无法跨越mask中的非0像素。例如，一个边缘检测的结果可以作为mask来阻止边缘填充。在输出中，mask中与image中填充像素对应的像素点被设置为1，或者flags标志位中设置的值(详见flags标志位的解释)。此外，该函数还用1填充了mask的边缘来简化内部处理。因此，可以在多个调用中使用同一mask，以确保填充区域不会重叠。
#seedPoint 起始像素点
#newVal   重绘像素区域的新的填充值(颜色)
#rect      可选输出参数，返回重绘区域的最小绑定矩形。
#loDiff     当前选定像素与其连通区中相邻像素中的一个像素，或者与加入该连通区的一个seedPoint像素，二者之间的最大下行差异值。
#upDiff    当前选定像素与其连通区中相邻像素中的一个像素，或者与加入该连通区的一个seedPoint像素，二者之间的最大上行差异值。
#flags     flags标志位是一个32bit的int类型数据，其由3部分组成： 0-7bit表示邻接性(4邻接、8邻接)；8-15bit表示mask的填充颜色；16-31bit表示填充模式（详见填充模式解释）
