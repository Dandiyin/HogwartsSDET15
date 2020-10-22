# -*- coding: utf-8 -*-
import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(scope="function", params=['Dandi', 'hhhhhh'])
def login(request):
    # 相当于setup操作
    print("登陆操作")
    username = request.param
    # 相当于return操作
    yield username
    # 相当于teardown操作
    print("退出登陆")


# @pytest.fixture(autouse=True, scope="session")
@pytest.fixture(scope="session")
def conn_db():
    print("完成数据库连接")
    yield
    print("关闭数据库连接")


@pytest.fixture(scope="module")
def get_cacl():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")
