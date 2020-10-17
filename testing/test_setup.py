# -*- coding: utf-8 -*-

# 模块级别（每个.py文件是一个模块）
def setup_module():
    print("资源准备：setup_module")


def teardown_module():
    print("资源销毁：teardown_module")


def test_case1():
    print("case1")


# 函数级别
def setup_function():
    print("资源准备：setup_function")


def teardown_function():
    print("资源销毁：teardown_function")


class TestDemo:

    # 类级别
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 方法级别  setup是setup_method的简写方式
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")


class TestDemo1:

    # 类级别
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 方法级别
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")
