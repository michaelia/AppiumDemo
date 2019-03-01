from common import Element
from common import device_congfigure
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import yaml
from common import  opeara
import allure


# -*- coding: UTF-8 -*-


# class SimpleIOSTests(unittest.TestCase):


    # def setUp(self):
    #
    #     device_congfigure.device().devices()
        # self.ele = Element.Element()

    # @classmethod
    # def setUpClass(cls):
    #     Element.Element(cls.device)

        # print(self.drive)

    # def test_Login(self):
    #
    #     time.sleep(5)
    #     opearaObject = opeara.opeara()
    #     opearaObject.option()
    #     time.sleep(15)
        # login_button=(By.ID,'sg.bigo.live:id/rl_login_3')
        # phone_button=(By.ID,'sg.bigo.live:id/et_phone_num')
        # phone_login_button=(By.ID,'sg.bigo.live:id/tv_next')
        # phone_password_button=(By.ID,'sg.bigo.live:id/et_password')
        # phone_password_button_login=(By.ID,'sg.bigo.live:id/tv_next')
        # ele=Element.Element()
        # ele.clickButton(login_button)
        # ele.send_keys(phone_button,'15889950702')
        # ele.clickButton(phone_login_button)
        # ele.send_keys(phone_password_button,'zmy630702')
        # ele.clickButton(phone_password_button_login)
        # time.sleep(15)


    # def tearDown(self):
    #     self.device.quit()


@allure.feature('feature1')
class TestClass(object):



    opearaRead = opeara.opeara()
    loginCase =opearaRead.read()

    @pytest.fixture(params=loginCase,autouse=True)
    @allure.step('登录')
    def getData(self,request):
        print(request.param)
        self.opearaRead.option(request.param)


    def test_Login(self,getData):
        time.sleep(5)
        getData
        time.sleep(15)


    # def test_option(self):
    #     time.sleep(5)
    #     opearaObject = opeara.opeara()
    #     opearaObject.option()
    #     time.sleep(15)

if __name__ == '__main__':
    # T=TestClass()
    # pytest.main()
    pytest.main(['-s', '-q', '--alluredir', './report'])
    # suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    # unittest.TextTestRunner(verbosity = 2).run(suite)