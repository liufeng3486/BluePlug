#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,sys
from Base import *
import SubMom

class MainQuest(SubMom.SubMom):
    def run(self):
        self.spec_dict = {
            "Spec_1": [
                [745, 460], [174, 152, 121],
                [750, 460], [143, 129, 98],
                [755, 460], [171, 154, 108],"tesx1"],
            "spec_q_2": [
                [34, 333], [245, 226, 166],
                [50, 333], [229, 212, 156],
                [71, 333], [254, 234, 172],"text2" ],
            "zhi_1": [
                [16, 334], [223, 205, 151],
                [14, 337], [224, 206, 152],
                [19, 337], [208, 191, 141], "text3"],
        }
        try:
            state = self.setup()
            if state[0] == "spec_q_1":
                self.click("750 40")
            elif state[0] == "spec_q_2":
                self.click("45 165")
                time.sleep(2)
                self.click("250 230")
                return "MainQuest"
            elif state[0] == "zhi_1":
                self.click("39 218")
                time.sleep(20)
                return "MainQuest"
            elif state[0]:
                print("get ok :",state)
                if  state[0] != "talk" and "pet_together_" not in state[0] and state[0] != "tower_fighter":

                    self.click(state[1])
                elif state[0] == "sign_sele":
                    pass
                elif state[0] == "talk":
                    self.click("380 220")
                    self.click("380 220")
                    self.click("380 220")
                else:
                    self.click(state[1])
            else:
                prt("no")
                self.click("45 165")
            return "MainQuest"
        except Exception as ex:
            print(str(ex))
            return False


if __name__ == '__main__':
    a = MainQuest(0)
    a.run()