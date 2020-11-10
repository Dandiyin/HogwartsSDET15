# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(autouse=True, scope="session")
def conn_db():
    print("完成数据库连接aaaaa")
    yield
    print("关闭数据库连接aaaaa")
