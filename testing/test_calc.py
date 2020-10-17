# -*- coding: utf-8 -*-
import pytest

from pythoncode.calculator import Calculator


def test_a():
    print("aaaaa")


class TestCalc:

    def setup(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [10000000, 10000000, 20000000], [0.1, 0.1, 0.2], [-1, -1, -2], [1, 0, 1]],
                             ids=['int_case', 'big_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 1], [1000000, 1000, 1000], [-1, -1, 1], [-1, 1, -1], [0, 2, 0], [2, 0, 0],
                              [0, 0, 0],
                              [0.1, 0.2, 0.5], [-0.2, -0.5, 0.4], [-0.1, 0.1, -1], [-0.2, 2, -0.1]])
    def test_div(self, a, b, expect):
        if b == 0:
            print("0不能做除数")
        else:
            result = self.calc.div(a, b)
            assert result == expect

    # def test_add1(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
