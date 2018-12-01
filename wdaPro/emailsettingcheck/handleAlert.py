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


driver = wda.Client('http://localhost:8100')
session_app = driver.session('com.tencent.qqmail.dailybuild')


def alert_callback(session):
    btns = set([u'不再提醒', 'OK', u'知道了', 'Allow', u'允许']).intersection(session.alert.buttons())
    if len(btns) == 0:
        raise RuntimeError("Alert can not handled, buttons: " + ', '.join(session.alert.buttons()))
    session.alert.click(list(btns)[0])


def handle_alert():
    btns = session_app.alert.buttons()
    print "Alert buttons", btns
    if u"好" in btns:
        session_app.alert.click(u"好")
    else:
        session_app.alert.accept()


session_app.set_alert_callback(alert_callback)
# session_app.alert_callback = handle_alert


# session_app.set_alert_callback(alert_callback)
session_app(name=u'选项菜单').click()
session_app(name=u'设置').click()
session_app.tap(200, 90)
session_app(name=u'头像').click()
session_app(name=u'从手机相册选取').click()
session_app.tap(200, 640)
time.sleep(3)
session_app(name=u'取消').click()
session_app(name=u'头像').click()
session_app(name=u'拍照').click()
session_app(name=u'取消').click()
session_app(name=u'设置').click()

