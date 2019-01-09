#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Operate.PageOperate import PageOperate
from Base.BaseReplace import ReplaceYaml



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

tc_temp = PATH("../../yamls/temp.yaml")
el_android = PATH("../../yamls/xky_android.yaml")
el_iOS = PATH("../../yamls/el_iOS.yaml")

class LoginTest(ParametrizedTestCase):

    def repalce(self, tc, tc_temp):
        if self.platformName == 'android':
            ReplaceYaml(tc, tc_temp, el_android)
        elif self.platformName == 'iOS':
            ReplaceYaml(tc, tc_temp, el_iOS)

    def test_login(self):
        tc = PATH("../../yamls/Android/test_login/test_login.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()



    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()



if __name__ == '__main__':
    pass
