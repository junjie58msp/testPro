# coding:utf-8

import unittest
import os
import sys


class MyTestFunction(unittest.TestCase):
    def setUp(self):
        print "begin"

    def tearDown(self):
        print "end"

    def test_add(self):
        print "add"


if __name__=="__main__":
    A = MyTestFunction()
    A.test_add()
    print "hello"
    print u"谢谢"
    print "xiexie"
