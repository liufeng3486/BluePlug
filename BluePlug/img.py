#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import os
import numpy as np,time
from BluePlug.Base import *
path = "./test/"
mkdir(path)
def set_file_name(file_dir): #获取文件目录
    for root, dirs, files in os.walk(file_dir):
        pass
    temp = []
    for i in files:
        if "source_" not in i and ".bmp" in i:
            temp.append(i.split(".")[0])
    return temp
def get_image():
    os.popen('.\dnplayer2\dnconsole.exe adb --index 0  --command "shell /system/bin/screencap -p /sdcard/screenshot.png"')
    os.popen('.\dnplayer2\dnconsole.exe adb --index 0  --command "pull /sdcard/screenshot.png %sscreenshot_2.png"'%path)
    # pngTranspose("d:/ChangZhi/4/screenshot_2.png") #横版竖版匹配

def get_image_array(path):
    im = Image.open(path, "r")
    img_array = np.array(im)
    return img_array

def messageSave(box,name,file=path+"read.txt"):
    with open(file,"a+") as message_file :
        message_file.write(name+"\t"+str(box)+"\n")
def image_save(box,name="skip"):
    for i in box:
        if i%10 != 0 :
            print("坐标必须是10的整数倍")
            return False
    set_name = set_file_name(path) #该目录下不要建立二级目录
    if name in set_name:
        print("重名")
        return False
    im = Image.open(path+"screenshot_2.png", "r")
    im.save(path+"source_%s.png"%name)
    region = im.crop(box)
    region.save(path+'%s.bmp'%name)
    messageSave(box,name)
    print ("裁剪完成,名称:%s.bmp;裁剪区域:%s"%(name,str(box)))


#1截图，2彩图,3 获取坐标颜色
def test_iamge(type=1,addr = [480,460],limit=10,name="test",location=[[1,2],[2,3]]):
    a = addr[0]
    b = addr[1]
    box = (a,b,a+limit,b+limit)
    if type == 1:
        get_image()
    elif type == 2:
        image_save(box,name)
    elif type == 3:
        pass





