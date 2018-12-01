#! /usr/bin/python
# -*- coding:utf-8 -*-
# filename : testios.py
# author: hyper
# createdate: 2017/02/22

from wdaPro import wda
import time

# configuration
wda.DEBUG = False
wda.HTTP_TIMEOUT = 60.0

if __name__ == '__main__':
    # bundle_id = sys.argv[1]
    # bundle_id = 'com.tencent.qqmail'
    # driver = wda.Client('http://localhost:8100')
    # # open app
    # session_app = driver.session(bundle_id)
    #
    # # get screen size
    # height = session_app.window_size().height
    # width = session_app.window_size().width
    # print height, width
    # width, height = session_app.window_size()
    # print width, height
    #
    # # # one of <portrait & landscape>
    # # if session_app.orientation == wda.PORTRAIT:
    # #     session_app.orientation = wda.LANDSCAPE
    #
    # # simulate touch at point
    # # session_app.tap(50, 700)
    # # double touch
    # # session_app.double_tap(50, 700)
    # # tap_hold
    # # session_app.tap_hold(200, 50, 1)
    #
    # # simulate swipe
    # # session_app.swipe(50, 100, 50, 700)
    # # session_app.swipe_down()
    # # session_app.swipe_up()
    # # session_app.swipe_left()
    # # session_app.swipe_right()
    #
    # # get page source
    # # driver.source(accessible=True)  # raise exception
    # # driver.screenshot('filename.png')  # try to screen but not successfully saved in gallery
    # # time.sleep(3)
    # session_app.swipe(50, 300, 50, 400, 2)
    # # element wait for searched and click(alias of tap)
    # e0 = session_app(name=u"搜索").click()
    #
    # e_1 = session_app(name=u"搜索")
    # e_1.set_text('hello')
    # e_1.set_text('world xxx')
    # e_1.set_text('\b\b\b')
    # e_1.clear_text()
    # e_1.set_text('helloWorld')
    # # e_1.set_text('hello')
    # print 'hello'
    # time.sleep(3)
    # try:
    #     session_app(name=u'搜索').click_exists()
    # except:
    #     raise wda.WDAElementNotFoundError
    # else:
    #     print "find 搜索"
    # session_app(name=u'取消').click_exists()
    #
    # e1 = session_app(name=u"重要联系人").get(timeout=3)
    # e1.tap()
    # e2 = session_app(name=u"返回").get(timeout=3)
    # e2.tap()
    # session_app.swipe(50, 300, 50, 100, 2)
    # e3 = session_app(name=u"哈哈哈哈").get(timeout=20)
    # e3.tap()
    # e2.tap()
    # # e4 = session_app(predicate='name LIKE u\"*多应*\"').get(timeout=5) not ok
    # # e4.tap()
    # print session_app(text=u'哈哈哈哈').exists
    # print session_app(text=u'哈哈哈哈').find_elements()
    #
    # # set default timeout
    # # session_app.set_timeout(5)
    # session_app.close()

    print 'success'
    driver = wda.Client('http://localhost:8100')
    setting_session = driver.session('com.tencent.xin')
    setting_session.swipe(50, 100, 50, 200)
    setting_session(nameContains=u"孙宝宝").click_exists(5)
    setting_session.tap(150, 600)
    time.sleep(3)
    setting_session.close()







