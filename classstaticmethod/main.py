# coding:utf-8

class A(object):
    num = 1
    def __init__(self, inputvalue):
        self.value = inputvalue
        print("init method")
    def instance_method(self):
        print("instance method")
        print(self.value)
    @staticmethod
    def static_function():
        print("static method")
        print(A.num)
        print(A(4).instance_method())
    @classmethod
    def class_method(cls):
        print("class method")
        print(A.num)
        print(cls(5).instance_method())
A.static_function()
A.class_method()
A(4).instance_method()