# -*- coding: utf-8 -*-
import os

import allure
import pytest
import yaml


# from pythoncode.calculator import Calculator


# 解析测试数据文件
def get_datas():
    with open("./datas/calc.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    # add_datas = datas['add']['datas']
    # add_ids = datas['add']['ids']
    # add_float_datas = datas['add_float']['datas']
    # div_datas = datas['div']['datas']
    # div_zero_datas = datas['div_zero']['datas']
    # return [add_datas, add_ids, add_float_datas, div_datas, div_zero_datas]
    return datas


# 解析测试步骤文件
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if 'add' == step:
            print("step: add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a, b)
        assert expect == result


@allure.feature("计算器测试用例")
class TestCalc:

    # def setup(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown(self):
    #     print("计算结束")
    @allure.story("加法")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()['add']['datas'],
                             ids=get_datas()['add']['ids'])
    def test_add(self, get_cacl, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_cacl.add(a, b)
        assert result == expect

    # @pytest.mark.parametrize('a,b,expect', [
    #     [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]])
    @allure.story("加法--浮点数")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'])
    def test_add_float(self, get_cacl, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_cacl.add(a, b)
        assert round(result, 2) == expect

    @allure.story("减法")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()['sub']['datas'])
    def test_sub(self, get_cacl, a, b, expect):
        # calc = Calculator()
        # result = self.calc.sub(a, b)
        result = get_cacl.sub(a, b)
        assert round(result, 2) == expect

    @allure.story("乘法")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_datas()['mul']['datas'])
    def test_mul(self, get_cacl, a, b, expect):
        # calc = Calculator()
        # result = self.calc.mul(a, b)
        result = get_cacl.mul(a, b)
        assert round(result, 4) == expect

    # @pytest.mark.parametrize('a,b,expect',
    #                          [[1, 1, 1], [1000000, 1000, 1000], [-1, -1, 1], [-1, 1, -1], [0, 2, 0],
    #                           [0.1, 0.2, 0.5], [-0.2, -0.5, 0.4], [-0.1, 0.1, -1], [-0.2, 2, -0.1]])
    @allure.story("除法")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()['div']['datas'])
    def test_div(self, get_cacl, a, b, expect):
        # result = self.calc.div(a, b)
        result = get_cacl.div(a, b)
        assert result == expect

    # @pytest.mark.parametrize('a,b', [[2, 0], [0, 0], [0.1, 0]])
    @allure.story("除法--0做除数")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b', get_datas()['div_zero']['datas'])
    def test_div_zero(self, get_cacl, a, b):
        with pytest.raises(ZeroDivisionError):
            print("0不能做除数！")
            # self.calc.div(a, b)
            get_cacl.div(a, b)

    # 测试步骤驱动
    def test_add_steps(self, get_cacl):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", get_cacl, a, b, expect)
        # 三个测试步骤
        # assert 2 == self.calc.add(1, 1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add(-1, 1)

    # def test_add1(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
