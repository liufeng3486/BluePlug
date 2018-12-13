#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np

from PIL import ImageFile
# import fork
class Base():
    def __init__(self):
        pass
    @staticmethod
    def getPngRgbList(path):
        im = Image.open(path, "r")
        im = im.convert("RGB")
        im_list = np.array(im).tolist()
        return im_list
    @staticmethod
    def getPoint(path,point_list):
        if path == "test":
            path = "./test/screenshot_2.png"
        im_list = Base.getPngRgbList(path)
        for index in range(0, len(point_list), 2):
            print ("坐标:",point_list[index],point_list[index+1])
            print ("RGB:",im_list[point_list[index]][point_list[index+1]])
        print("[")
        for index in range(0, len(point_list), 2):
            print("[", point_list[index],",", point_list[index + 1],"],",end="")
            print( im_list[point_list[index]][point_list[index + 1]],",")
        print("]")
            # if not pix_assert(im_list[add[0]][add[1]], point_list[index + 1]):
            #     return False
        return True
def get_image_array(path): #图片转np.array
    im = Image.open(path, "r")
    img_array = np.array(im)
    return img_array

def pix_assert(point1,ponit2,tag=10): #判点相似度
    for index,i in enumerate(point1):
        if abs(point1[index]-ponit2[index]) > tag:
            return False
    return True

def file_name(file_dir): #获取文件目录
    for root, dirs, files in os.walk(file_dir):
        pass
    temp = []
    for i in files:
        if "source_" not in i and ".bmp" in i:
            temp.append(file_dir+"\\"+i)
    return temp

def pngTranspose(path):#旋转自适应

    ImageFile.LOAD_TRUNCATED_IMAGES = True
    img = Image.open(path) #截图旋转
    size = img.size
    # print(size)
    if size[0] < size[1]:
        print("size[0] < size[1] transpose")
        out1 = img.transpose(2)
        out1.save(path)


def get_image(index=0,name="screenshot.png",watchdog=False):#获取图片
    os.popen('.\dnplayer2\dnconsole.exe adb --index %s  --command "shell /system/bin/screencap -p /sdcard/screenshot.png"'%str(index))
    os.popen('.\dnplayer2\dnconsole.exe adb --index %s  --command "pull /sdcard/screenshot.png ./%s/%s"'%(str(index),str(index),name))
    pngTranspose("./%s/%s"%(str(index),name))
    # print ("111")


def prt(*data,channel=False):
    # if type(data[-1])==pyqtBoundSignal:
    #     channel = data[-1]#
    #     data=data[:-1]# 标准化打印
    if not channel:
        for i in data:
            print(str(i), )
    else:
        temp_str = ""
        for i in data:

            temp_str =  temp_str + str(i) +" "
        temp_str += "\n"
        # channel.emit(temp_str)
        # print (str(i),)


def click(temp,index=0):#点击操作
    prt("clikc:",temp)
    string ='.\dnplayer2\dnconsole.exe adb --index %s  --command "shell input tap %s "'%(str(index),temp)
    os.popen(string)

def three_point_check(point1,rgb1,point2,rgb2,point3,rgb3,index=0):#三点比对
    try:

        get_image()
        im = Image.open(".\\%s\\screenshot.png"%str(index), "r")
        im = im.convert("RGB")
        im_list = np.array(im).tolist()
        print(im_list[point1[0]][point1[1]],im_list[point2[0]][point2[1]],im_list[point3[0]][point3[1]])
        if (pix_assert(im_list[point1[0]][point1[1]],rgb1)) \
                and (pix_assert(im_list[point2[0]][point2[1]], rgb2)) \
                and (pix_assert(im_list[point3[0]][point3[1]], rgb3)):
            return True
        return False
    except Exception as ex:
        prt(str(ex))
        return  False

def morePointCheck(point_list,index=0):
    try:
        im_list = Base.getPngRgbList(".\\%s\\screenshot.png"%str(index))
        if len(point_list)==0 or len(point_list)%2 != 0:
            prt(point_list,"not match")
            return False
        for index in range(0,len(point_list),2):
            add = point_list[index]
            if not pix_assert(im_list[add[0]][add[1]],point_list[index+1]):
                return False
        return True
    except Exception as ex:
        prt(str(ex))
        return  False

def boxPng(path,box,name,index=0):
    try:
        im = Image.open(path, "r")
        region = im.crop(box)
        new_file_path = ".\\%s\\%s.png"%(str(index),name)
        region = region.transpose(2)
        region.save(new_file_path)
        return new_file_path
    except:
        return False
def getLv(path):
    try:
        new_file_path = boxPng(path,[457,75,472,96],'Lv')
        if new_file_path:
            lv = fork.getcharactor(new_file_path)
            if len(lv)>0:
                return lv[0]
        prt("Lv get false")
        return False
    except:
        return False
def getFpoint(path):
    try:
        new_file_path = boxPng(path,[413,92,431,159],'Lv')
        if new_file_path:
            lv = fork.getcharactor(new_file_path)
            if len(lv)>0:
                return lv[0]
        prt("Fpoint get false")
        return False
    except:
        return False
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


if __name__ == '__main__':
    print (morePointCheck([1,2,3,4,5,6]))