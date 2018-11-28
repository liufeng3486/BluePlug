#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time
from Base import *
from FindAxis import *
# from ChooseZone import *

import SubMom

class Login(SubMom.SubMom):

    def run(self):
        try:
            state = self.setup()

            note_dict = {"login_notice_close": "发现登陆公告，关闭",  # 登陆后的公告关闭按钮
                         "login_enter_game": "登陆游戏",  # 登陆游戏
                         "welfare_close": "关闭福利窗口",  # 福利窗口关闭按钮
                         "offline_notice_close": "接收离线经验",
                         "login_already_online": "用户已登录，强行登录",
                         }  # 离线经验提示关闭

            # activit 用来判断登陆成功
            if state[0] in note_dict:
                print (note_dict[state[0]])
            else:
                print(state[0])
            if state[0] and "_check" not in state[0]:
                self.click(state[1])
                self.finish = self.finish_limit
            elif state[0] and "new_user_check" in state[0]:
                self.finish -= 1
                login_state = "New_Init"
            elif state[0] and "login_check" in state[0]:
                self.finish -= 1
                login_state = "Old"
            elif state[0] and "talk_check" in state[0]:
                self.finish -= 1
                login_state = "New_Start"
            else:
                self.finish -= 1
                print("----1")
                login_state = False
            if self.finish < 1:
                return  "MainQuest"
            return "Login"
        except Exception as ex:
            print(str(ex))
            return False

if __name__ == '__main__':
    pass