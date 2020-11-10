# -*- coding: utf-8 -*-


# 使用了装饰器就没办法打印fixture的返回值了
# 如果测试用例里，需要用到fixture的返回值 的话，fixture的名字需要以参数的形式传入到方法里，不能使用装饰器的方式。
import pytest


# @pytest.mark.usefixtures("login")
def test_case1(login):
    print(login)
    print("用例1")


def test_case2():
    print("用例2")


def test_case3(conn_db):
    # 打印出None是因为conn_db没有返回值
    print(conn_db)
    print("用例3")
