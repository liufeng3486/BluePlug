#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,sys
from BluePlug.Base import *
from BluePlug.FindAxis import *
#子方法父类
class SubMom(object):
    def __init__(self,index,self_image=False,screenshot=False):
        self.filename = ".\\bmp\\"+self.__class__.__name__ #获取bmp路径
        self.self_image = self_image
        self.screenshot = screenshot
        self.index = index  #设备号
        self.bmp_dir_list = self.getImagePath() #获取bmp路径列表。可能存在多个子目录
        self.bmp_list = self.getIamgeList()#获取bmp列表。和路径一一对应
        self.spec_dict={}   #三点确定的列表
        self.image_path = ".\\%s\screenshot.png" % str(self.index)
        if self.self_image:
            self.image_path = self.self_image
        self.finish = 10
        self.finish_limit=10
    def getIamgeList(self):
        bmp_list = []
        for solo_bmp_dir in self.bmp_dir_list:
            bmp_list.append(file_name(solo_bmp_dir))
        return bmp_list
    def spec_test(self,point1,point2,point3,filepath=False):  #用来获取三点RGB的方法。filepath不填，就是默认的截图
        if not filepath:
            im = Image.open(self.image_path, "r")
        else:
            im = Image.open(filepath, "r")
        im = im.convert("RGB")
        im_list = np.array(im).tolist()
        print (point1,",",im_list[point1[0]][point1[1]],",")
        print(point2, ",", im_list[point2[0]][point2[1]], ",")
        print(point3, ",", im_list[point3[0]][point3[1]], ",")

    def spec_check(self): #三点判断

        im = Image.open(self.image_path, "r")
        im = im.convert("RGB")
        im_list = np.array(im).tolist()
        for solo_spec in self.spec_dict:
            if (pix_assert(im_list[self.spec_dict[solo_spec][0][0]][self.spec_dict[solo_spec][0][1]], self.spec_dict[solo_spec][1])) \
                    and (pix_assert(im_list[self.spec_dict[solo_spec][2][0]][self.spec_dict[solo_spec][2][1]], self.spec_dict[solo_spec][3])) \
                    and (pix_assert(im_list[self.spec_dict[solo_spec][4][0]][self.spec_dict[solo_spec][4][1]], self.spec_dict[solo_spec][5])):
                print(self.spec_dict[solo_spec][6])
                return solo_spec,True
        return False,False
    def click(self,temp): #click
        print("click add:", temp)
        string = '.\dnplayer2\dnconsole.exe adb --index %s  --command "shell input tap %s "' % (str(self.index), temp)
        os.system(string)

    def setup(self):  #初始化
        if self.screenshot:
            get_image(self.index)
        spec_state = self.spec_check()  #三点判断
        if spec_state[0]:
            return spec_state
        # im = Image.open(".\\%s\screenshot.png" % (str(self.index)), "r")
        if len(self.bmp_dir_list) > 1:  #多个bmp文件
            for temp_bmp in self.bmp_list:
                state = find_sub_graphes(self.image_path, temp_bmp)
                if state[0]:
                    return state
        else:   #一个bmp文件
            state = find_sub_graphes(self.image_path,  self.bmp_list[0])
            if state[0]:
                return state
        return False, False
    def getImagePath(self):
        try:
            dir_list = []
            temp_list = os.listdir(self.filename)
            for solo in temp_list:
                if os.path.isdir(self.filename+"\\"+solo):
                    dir_list.append(self.filename+"\\"+solo+"\\")
            if dir_list:
                dir_list.sort()
                return dir_list
            else:
                return [self.filename]
        except Exception as ex:
            print ("bmp filename error:",ex)

    def run(self):
        pass

if __name__ == '__main__':
    a  = SubMom(0)
    a.spec_test([22,33],[33,44],[44,55],filepath=".\\0\\screenshot.png") #获取图片的3点RGB
    print (a.getImagePath())





