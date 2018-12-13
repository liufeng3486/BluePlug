import os,time
from BluePlug.Base import *
class BaseClass():
    class Init(object):
        def __init__(self,index,app="",path = ".\dnplayer2\dnconsole.exe",channel=False):
            self.index = index
            self.channel = channel
            self.app = app
            self.mock_path = "%s launch --index %s" % (path,str(index))
            self.setup()
        def setup(self):
            self.check_list = [[36, 466], [255, 247, 186],
                                          [47, 465], [255, 247, 186],
                                          [50, 459], [195, 157, 121]]
            pass

        def start_mock(self):
            os.popen(self.mock_path)
        def sysPrint(self,*data):
            prt(*data,self.channel)
        def start_app(self):
            try:
                string = '.\dnplayer2\dnconsole.exe adb --index %s  --command "shell am start -n %s"' % (str(
                    self.index),self.app)
                print (string)
                result = os.popen(string)
                res = result.read()
                print (res.splitlines())
                for line in res.splitlines():
                    if "found" in line:
                        return False
                    if "Starting" in line:
                        return True
            except:
                return False

        def init_start(self):
            # self.index = index
            self.start_mock()
            self.sysPrint("Mock Start Up")
            for i in range(10):
                time.sleep(5)
                self.sysPrint("Try APP Start Up:", self.app)
                if self.start_app():
                    i = 10
                    return "Init_check"
                else:
                    self.sysPrint("Mock Starting...")
            self.sysPrint("Mock Start Up TimeOut")
            return False

        def start_check(self):
            # self.index = index
            self.setup()
            try:
                for i in range(20):
                    time.sleep(1)
                    if morePointCheck(self.check_list,index=self.index):
                        self.sysPrint("APP Start Ok")
                        return "Login"
                    else:
                        self.sysPrint("APPing.....")
                self.sysPrint("APP TimeOut")
                return "Init.start_check Error"
            except Exception as ex:
                self.sysPrint("start_check false", str(ex))
                return "Init.start_check Error"