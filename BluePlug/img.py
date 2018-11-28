#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import os
import numpy as np,time
from Base import *
def set_file_name(file_dir): #获取文件目录
    for root, dirs, files in os.walk(file_dir):
        pass
    temp = []
    for i in files:
        if "source_" not in i and ".bmp" in i:
            temp.append(i.split(".")[0])
    return temp
def get_image():
    os.system('.\dnplayer2\dnconsole.exe adb --index 0  --command "shell /system/bin/screencap -p /sdcard/screenshot.png"')
    os.system('.\dnplayer2\dnconsole.exe adb --index 0  --command "pull /sdcard/screenshot.png d:/ChangZhi/4/screenshot_2.png"')
    # pngTranspose("d:/ChangZhi/4/screenshot_2.png") #横版竖版匹配

def get_image_array(path):
    im = Image.open(path, "r")
    img_array = np.array(im)
    return img_array

def messageSave(box,name,file=".\\4\\read.txt"):
    with open(file,"a+") as message_file :
        message_file.write(name+"\t"+str(box)+"\n")
def image_save(box,name="skip"):
    for i in box:
        if i%10 != 0 :
            print("坐标必须是10的整数倍")
            return False
    set_name = set_file_name(".\\4\\") #该目录下不要建立二级目录
    if name in set_name:
        print("重名")
        return False
    im = Image.open(".\\4\\screenshot_2.png", "r")
    im.save(".\\4\\source_%s.png"%name)
    region = im.crop(box)
    region.save('.\\4\\%s.bmp'%name)
    messageSave(box,name)
    print ("裁剪完成,名称:%s.bmp;裁剪区域:%s"%(name,str(box)))

d =2
a = 480
b = 640
limit = 10
box = (a,b,a+limit,b+limit)
#自动记录裁剪信息  同名截图查重
if d == 2:
    image_save(box,"plot_ing")
else:
    get_image()


# import time
# def getPicDict(rootpath:str):
#     res = []
#     for dirpath, dirnames, filenames in os.walk(path):
#         dicter = {}
#         for filename in filenames:
#             dicter.setdefault(filename.split('.')[0], os.path.join(dirpath, filename))
#         res.append(dicter)
#     return res

