#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from appium import webdriver
"""
More involved iOS tests, using UICatalog application.
"""
import unittest
from appium import webdriver
import time
import yaml

class device():

    deviceName ='18a2b9c8'

    def devices(self):
        '''
        获取
        :return:
        '''
        with open(r'./Source/deviceConfigure', "r+", encoding='utf-8') as f:
            res = yaml.load(f)
            print(res)
            self.driver = webdriver.Remote(
                        command_executor='http://127.0.0.1:4723/wd/hub',
                        desired_capabilities=
                            res.get('18a2b9c8')

                        )
        return self.driver

    # res = yaml.load(f)
# class ComplexIOSTests(unittest.TestCase):
#
#
#     fileName ='18a2b9c8'
#     def setUp(self):
#         # set up appium
#         # ** Important Note **
#         # Make sure you have build the UICatalog applcation in your local repository
#         with open(r'../Source/deviceConfigure', "r+", encoding='utf-8') as f:
#             res = yaml.load(f)
#         self.driver = webdriver.Remote(
#             command_executor='http://127.0.0.1:4723/wd/hub',
#             desired_capabilities=
#                 res.get('18a2b9c8')
#             )
#
#     def test_click(self):
#         for i in range(10):
#             time.sleep(5)
#             self.driver.execute_script("mobile: tap", {"y":82,
#                                                        "x": 192,
#                                                        "duration": 50})
#
#
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__=='__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(ComplexIOSTests)
#     unittest.TextTestRunner(verbosity=2).run(suite)
#
