from BluePlug.Base import *
import BluePlug
class NewPlug(BluePlug.Worker):
    def run(self):
        if not self.default_close.run():
            if self.cus_state == "Init_start":
                self.init.init_start()
                self.cus_state = "Init_check"
            elif self.cus_state == "Init_check":
                self.cus_state = self.init.start_check()
            elif self.cus_state:
                prt("error", channel=self.sinOut2)
            else:
                prt("dead",channel=self.sinOut2)
            print ("1")
        else:
            print ("default_close")
    def subJobInit(self):
        self.init = GmInit(self.index)
        self.default_close = BluePlug.BaseClass.DefaultClose(self.index)

class GmInit(BluePlug.BaseClass.Init):
    def setup(self):
        self.app = "com.tencent.mm/.app.WeChatSplashActivity"
        self.check_list=[
                        [ 1 , 2 ],[1, 3, 6] ,
                        [ 4 , 5 ],[1, 3, 6] ,
                        [ 400 , 400 ],[48, 64, 89] ,
                        ]
class Login(BluePlug.SubMom):
    @BluePlug.Base.executeCatch
    def run(self):
        state = self.setup()
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

if __name__ == '__main__':
    # a = BluePlug.test_iamge(type=1,addr = [480,460],limit=10,name="test")
    # a = BluePlug.test_iamge(type=2, addr=[480, 460], limit=10, name="test")
    # BluePlug.Base.getPoint("test",[1,2,4,5,400,400])
    a = NewPlug()
    a.cus_state = "Init_check"
    a.mainrun()





