#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author:罗徐 time:2019/6/4
# 实现模板匹配操作，从一个小的图片开始，在另一个图片里搜寻符合的图片
# 这个操作通过匹配算法实现，由于opencv实现的算法优越性，所以速度很快
import cv2 as cv
import numpy as np


def template_demo():
    tpl=cv.imread("C:/Users/17913/python+opencv/xuanji nian.png")
    # 被检索小图像
    target=cv.imread("C:/Users/17913/python+opencv/xuanji.png")
    # 目标图像
    cv.imshow("tpl",tpl)
    cv.imshow("target",target)
    methods=[cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    th,tw=tpl.shape[:2]
    # 获取模板的宽高
    for md in methods:
        print(md)
        result=cv.matchTemplate(target,tpl,md)
        # 核心函数
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        # 匹配的最小值与最大值
        if md == cv.TM_SQDIFF_NORMED:
            tl=min_loc
        else:
            tl=max_loc
            #tl是捕捉左上角的点，通过获取长宽高来找到右下角的点
        br=(tl[0]+tw,tl[1]+th)
        cv.rectangle(target,tl,br,(0,0,255),2)
        #绘制红矩形至图片上
        cv.imshow("motch-"+np.str(md),target)


src=cv.imread("C:/Users/17913/python+opencv/tangsan.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#cv.imshow("input image",src)
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
