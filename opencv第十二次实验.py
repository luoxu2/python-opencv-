#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/5/22
#图像直方图的应用：均衡化与比较
import cv2 as cv
import numpy as np


def equalhist_demo(image):
    #直方图均衡化可以提高对比度，只适用于双通道图像
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst=cv.equalizeHist(gray)
    #直方图均衡化函数
    cv.imshow("equalhist_demo",dst)

def create_rgb_hist(image):
    h,w,c=image.shape
    rgbHist=np.zeros([16*16*16,1],np.float32)
    bsize=256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index=np.int(b/bsize)*16*16+np.int(g/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0]=rgbHist[np.int(index),0]+1
    return rgbHist


def hist_compare(image1,image2):
    hist1=create_rgb_hist(image1)
    hist2=create_rgb_hist(image2)
    mach1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    #计算巴氏距离
    mach2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    #计算相关性
    mach3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    #计算卡方
    print("巴氏距离: %d ,相关性: %d,卡方: %d" % (mach1,mach2,mach3))

src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
src1=cv.imread("C:/Users/17913/python+opencv/tangsan1.png")
src2=cv.imread("C:/Users/17913/python+opencv/tangsan2.png")
cv.namedWindow("input image",0)
cv.imshow("input image",src)

equalhist_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
hist_compare(src1,src2)