import QtWork
import MainQuest,Login,Init

class Test(QtWork.Worker):
    def subJobInit(self):
        self.mainquest = MainQuest.MainQuest(self.index)
        self.login = Login.Login(self.index)
        self.init = Init.Init(self.index)
    def run(self, index=0, user_message=[]):  # index设备号  cus_state状态 0 未启动 1APP启动 2 登陆成功并获取初始状态
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
            print("error")
        else:
            print("dead",)

