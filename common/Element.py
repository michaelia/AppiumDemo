#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from dataclasses import dataclass
from dataclasses import field
from appium import webdriver
from common import device_congfigure
from selenium.webdriver.common.by import By
from common.logger import run_log as logger

class Element():

    driverNew=device_congfigure.device().devices()


    def find_element(self,loc):
        try:
            WebDriverWait(self.driverNew, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            logger.info('{}的元素已经找到了'.format(loc))
            return self.driverNew.find_element(*loc)
        except:
            logger.info(u"%s 页面中未能找到 %s 元素" % (self,loc))


    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            logger.info("%s 页面未能找到 %s 元素" % (self, loc))


    def clickButton(self, loc, find_first=True):
        try:
            print(loc)
            if find_first:
                self.find_element(loc)

            self.find_element(loc).click()
            logger.info('{}的元素在操作点击操作'.format(loc))
        except AttributeError:
            print("%s 页面未能找到 %s 按钮" % (self, loc))