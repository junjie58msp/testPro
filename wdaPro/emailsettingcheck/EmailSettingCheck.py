# coding:utf-8

import wda
import os
import sys
import unittest
import inspect
import time

# configuration
wda.DEBUG = False
wda.HTTP_TIMEOUT = 60.0


def alert_callback(onesession):
    print "in alert_callback"
    btns = set([u'不再提醒', 'OK', u'知道了', 'Allow', u'允许', u'好']).intersection(onesession.alert.buttons())
    if len(btns) == 0:
        raise RuntimeError("Alert can not handled, buttons: " + ', '.join(onesession.alert.buttons()))
    onesession.alert.click(list(btns)[0])


class EmailSettingCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = wda.Client('http://localhost:8100')
        self.session_app = self.driver.session('com.tencent.qqmail.dailybuild')
        self.session_app.set_alert_callback(alert_callback)
        pass

    def tearDown(self):
        self.session_app.close()
        pass

    def test_handle_alert(self):
        self.session_app(name=u'选项菜单').click_exists()
        self.session_app(name=u'设置').click_exists()
        print "xx"
        self.session_app.tap(200, 90)
        print "oo"
        self.session_app(name=u'头像').click_exists()
        self.session_app(name=u'从手机相册选取').click_exists()

        self.session_app.tap(200, 640)
        time.sleep(3)
        print "haha"
        pass

    @unittest.skip("for test")
    def test_login(self):
        # if not login then login
        # else pass
        funcname = inspect.stack()[0][3]+": "
        print funcname+"start check login"
        if self.session_app(text=u'选项菜单').exists:
            print funcname + "has login"
            pass
        elif self.session_app(text=u'添加帐户').exists:
            print funcname + "go login step"
            self.session_app(text=u'QQ邮箱').click_exists()
            self.session_app(text=u'帐号密码登录').click_exists()
            # account = self.session_app(,text=u'支持QQ号/邮箱/手机号登录')
            time.sleep(5)
            tempxx = self.session_app(name=u'登 录')
            tempxx.click_exists()
            print "xxoo"
            pass
        else:
            print funcname + "check has alert window"
            raise Exception("error")

