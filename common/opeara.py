#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from common import  Element
from selenium.webdriver.common.by import By

class opeara():
    path = ''
    def read(self):
        with open(r'./TestCase/LoginData', "r+", encoding='utf-8') as f:
            res = yaml.load(f)
            return res




    # def option(self):
    #     loginData = self.read()
    #     print(loginData)
    #     ele = Element.Element()
    #     for i in loginData:
    #         if 'click'  in loginData[i]:
    #             print(type(loginData[i][1]))
    #             ele.clickButton((By.ID,loginData[i][1]))
    #         elif 'send_keys' in loginData[i]:
    #             ele.send_keys((By.ID,loginData[i][1]),loginData[i][2])
    #

    def option(self,data):

        ele = Element.Element()
        if 'click'  in data:
            ele.clickButton((By.ID,data[1]))
        elif 'send_keys' in data:
            ele.send_keys((By.ID,data[1]),data[2])



if __name__ == '__main__':
    o= opeara()

    print(o.read())