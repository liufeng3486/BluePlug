#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time
from Base import *
#启动模拟器以及APP

class Init(object):
    def __init__(self,index):
        self.index = index

    def start_mock(self):

        string = ".\dnplayer2\dnconsole.exe launch --index %s" % str(index)
        os.system(string)

    def start_app(self, channel=False):
        # self.index = index
        try:
            prt("尝试启动APP", channel)
            string = '.\dnplayer2\dnconsole.exe adb --index %s  --command "shell am start -n com.tencent.xyj/.MGameActivity"' % str(
                index)
            result = os.popen(string)
            res = result.read()
            for line in res.splitlines():
                if "found" in line:
                    return False
                if "Starting" in line:
                    return True
        except:
            return False

    def init_start(self, channel=False):
        # self.index = index
        start_mock(index)
        prt("模拟器启动", channel)
        for i in range(10):
            time.sleep(5)
            if start_app(index):
                i = 10
                prt("APP启动", channel)
                return "Init_check"
            else:
                prt("模拟器启动中，APP启动延时等待", channel)
        prt("模拟器启动超时", channel)
        return False

    def start_check(self, channel=False):
        # self.index = index
        try:
            for i in range(20):
                time.sleep(1)
                if (three_point_check([36, 466], [255, 247, 186],
                                      [47, 465], [255, 247, 186],
                                      [50, 459], [195, 157, 121], index=index)):
                    prt("APP启动成功", channel)
                    return "Login"
                else:
                    prt("APP启动中", channel)
            prt("APP启动超时", channel)
            return "Init.start_check Error"
        except Exception as ex:
            prt("start_check false", str(ex), channel)
            return "Init.start_check Error"

def start_mock(index):
    string = ".\dnplayer2\dnconsole.exe launch --index %s"%str(index)
    os.system(string)

def start_app(index,channel=False):
    try:
        prt("尝试启动APP",channel)
        string = '.\dnplayer2\dnconsole.exe adb --index %s  --command "shell am start -n com.tencent.xyj/.MGameActivity"' % str(
            index)
        result = os.popen(string)
        res = result.read()
        for line in res.splitlines():
            if "found" in line:
                return False
            if "Starting" in line:
                return True
    except:
        return False

def init_start(index,channel=False):
    start_mock(index)
    prt("模拟器启动",channel)
    for i in range(10):
        time.sleep(5)
        if start_app(index):
            i=10
            prt("APP启动",channel)
            return "Init_check"
        else:
            prt("模拟器启动中，APP启动延时等待",channel)
    prt("模拟器启动超时",channel)
    return False

def start_check(index,channel=False):
    try:
        for i in range(20):
            time.sleep(1)
            if (three_point_check([36,466],[255, 247, 186],
                              [47,465],[255, 247, 186],
                              [50,459],[195, 157, 121],index=index)):
                prt("APP启动成功",channel)
                return "Login"
            else:
                prt("APP启动中",channel)
        prt("APP启动超时",channel)
        return "Init.start_check Error"
    except Exception as ex:
        prt("start_check false",str(ex),channel)
        return "Init.start_check Error"

if __name__ == '__main__':
    cus_state = 0
    index = 0
    # global cus_state
    if cus_state == 0:
        if(init_start(index)):
            if(start_check(index)):
                cus_state = 1
    if cus_state == 1:
        pass
