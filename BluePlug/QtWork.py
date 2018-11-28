from PyQt5 import QtCore
from BluePlug.Base import *
import BluePlug.Init as Init
import BluePlug.Login as Login
# import Answer,DailyQuest,PetFight,PlotCopy
# import SetInit
import BluePlug.MainQuest as MainQuest
# import CreateRole as CreateRole
import time,shutil

class Worker(QtCore.QThread):
    sinOut = QtCore.pyqtSignal(str) # 自定义信号，执行run()函数时，从相关线程发射此信号
    sinOut2 = QtCore.pyqtSignal(str)
    # sinOut2 = "ddd"
    def __init__(self,index=0, parent=None):
        super(Worker, self).__init__(parent)
        self.start = time.time()
        self.index = index
        self.cus_state = "Wait"
        self.old_state = "Wait"
        self.counter = -1
        self.temp_counter = -1
        self.working = True
        self.function_1 = True
        self.function_2 = True
        self.function_3 = True
        self.function_4 = True
        self.function_5 = True
        self.lv = 0
        self.fpoint = 0
        self.dail_end = 0
        self.time_sleep = 1.5
        self.function_list = [ self.function_1 ,self.function_2 ,self.function_3 ,self.function_4 ,self.function_5 ]
        self.num = 0
        self.list =[True,True,True,True,True] #skip,talk*3
    def __del__(self):
        self.working = False
        self.wait()
    def setValue(self,index,value):
        # print("set",index,value)
        # self.function_1 = 111
        self.function_list[index] = value
        # print("ddd:",self.function_1)
    def getLvAndFpoint(self):
        try:
            lv = str(getLv(".//%s//screenshot.png" % str(self.index)))
            fpoint = getFpoint(".//%s//screenshot.png" % str(self.index))
            lv_int = int(lv)
            fpoint_int = int(fpoint)
            self.lv = lv
            self.fpoint = fpoint
        except:
            pass

    def get_image(self,name="screenshot.png"):  # 获取图片
        print("get image")
        os.system(
            '.\dnplayer2\dnconsole.exe adb --index %s  --command "shell /system/bin/screencap -p /sdcard/screenshot.png"' % str(
                self.index))
        os.system(
            '.\dnplayer2\dnconsole.exe adb --index %s  --command "pull /sdcard/screenshot.png d:/ChangZhi/%s/%s"' % (
            str(self.index), str(self.index), name))
        pngTranspose("d:/ChangZhi/%s/%s" % (str(self.index), name))
        print (time.time() - self.start )
        if time.time() - self.start > 600:
            print("get error log")
            self.start = time.time()
            shutil.copyfile("d:/ChangZhi/%s/%s" % (str(self.index), name), "d:/ChangZhi/%s/%s"%(str(self.index),str(int(time.time()))+".png"))
            # with open("d:/ChangZhi/%s/%s" % (str(self.index), name),"r")

    def subFunCall(self,func):
        if self.counter == -1:
            self.cus_state = func(self.index, channel=self.sinOut2)
            print ("subFunCall",self.cus_state)
        else:
            if self.temp_counter == -1 :
                self.temp_counter = self.counter
            self.temp_counter,self.cus_state = func(index = self.index,finish=self.temp_counter, channel=self.sinOut2)
            print("subFunCall",self.temp_counter,self.cus_state)


    def subJobInit(self):
        pass
        # self.mainquest = MainQuest.MainQuest(self.index)
        # self.login = Login.Login(self.index)
        # self.init = Init.Init(self.index)
    def mainrun(self):
        self.subJobInit()
        sign = 0
        while self.working == True:
            print(self.cus_state, "%" * 20)
            sign += 1
            self.get_image()
            if sign % 50 == 0:
                self.getLvAndFpoint()
            if self.old_state != self.cus_state:
                self.old_state = self.cus_state
                self.count = -1
            self.sleep((self.time_sleep))
            self.run()

    def run(self,index=0, user_message=[]):  # index设备号  cus_state状态 0 未启动 1APP启动 2 登陆成功并获取初始状态
        pass
        # if self.cus_state == "Init_start":
        #     self.init.init_start()
        # elif self.cus_state == "Init_check":
        #     self.init.start_check()
        # elif self.cus_state == "Login":
        #     self.login.run()
        # elif self.cus_state == "MainQuest":
        #     self.mainquest.run()
        # elif self.cus_state == "Wait":
        #     self.sleep(5)
        # elif self.cus_state:
        #     prt("error", channel=self.sinOut2)
        # else:
        #     prt("dead",channel=self.sinOut2)
        # print ("1")

class NewPlug(Worker):
    def run(self):
        if self.cus_state == "Init_start":
            self.init.init_start()
        elif self.cus_state == "Init_check":
            self.init.start_check()
        elif self.cus_state == "Login":
            self.login.run()
        elif self.cus_state == "MainQuest":
            self.mainquest.run()
        elif self.cus_state == "Wait":
            self.sleep(5)
        elif self.cus_state:
            prt("error", channel=self.sinOut2)
        else:
            prt("dead",channel=self.sinOut2)
        print ("1")

if __name__ == '__main__':
    a = NewPlug()
    a.cus_state = "MainQuest"
    a.mainrun()
