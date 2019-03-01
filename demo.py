#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# class TestClass(object):
    # @pytest.fixture(params=[{'username':'zhouminyi','password':123456,},{'username':'zhouminyi','password':32134}])
    # def add(self,request):
    #
    #     user = request.param['username']
    #     pass1 = request.param['password']
    #     return '{}{}'.format(user,pass1)
    # add1= con.add



    # def test_result(self,run_add):
    #     print(type(run_add))
    #     result = run_add
    #     assert result =='zhouminyi32134'

#     @pytest.mark.parametrize("test_input,expected", [
#         ("3+5", 8),
#         pytest.param("6*9", 42, marks=pytest.mark.xfail),
#     ])
#     def add(self, request):
# #
#         sum =request.param + 4
#
#         return sum

    # def a(self,user,data,):
    #     if data:
    #         return True
    #     return False


    # @pytest.mark.parametrize("user", test_login_data)
    # def test_login(self,user, passwd):
    #     result=self.a(user, passwd)
    #     assert result == True

#     xfail = pytest.mark.xfail
#
#     @xfail
#     def test_hello(se):
#         assert 0
#
#     def test_one(self):
#         x = "this"
#         assert 'h' in x
#
#     @pytest.mark.skip(reason="no way of currently testing this")
#     def test_two(self):
#         add = lambda  x:x+1
#         assert add(4) == 6
#
#     @pytest.mark.skip(reason="no way of currently testing this")
#     def test_three(self):
#         assert 1 + 1e-8 == approx(1)
#
# @pytest.mark.parametrize("test_input,expected", [
#     ("3+5", 8),("7+2",9),("")
# #     pytest.param("6*9", 42, marks=pytest.mark.xfail),
# # ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

        # def test_zero_division(self):
        #     with pytest.raises(ZeroDivisionError):
        #         1 / 0
        #
        # def test_recursion_depth(self):
        #     with pytest.raises(RuntimeError) as excinfo:
        #         def f():
        #             f()
        #
        #         f()
        #     assert 'maximum recursion' in str(excinfo.value)

    # pytest.register_assert_rewrite("pytest_foo.helper")
    # def test_compare(self):
    #     f1 = Foo(1)
    #     f2 = Foo(2)
    #     assert f1 == f2

    # is_lead=[4,40,50,60,70]
    #
    # @pytest.fixture(params=is_lead)
    # def is_lead(self,req):
    #     return req
    #
    # def test_is_lead(self):
    #     assert self.is_lead()


    # def is_leap_year(year):
    #     # 先判断year是不是整型
    #     if isinstance(year, int) is not True:
    #         raise TypeError("传入的参数不是整数")
    #     elif year == 0:
    #         raise ValueError("公元元年是从公元一年开始！！")
    #     elif abs(year) != year:
    #         raise ValueError("传入的参数不是正整数")
    #     elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #         print("%d年是闰年" % year)
    #         return True
    #     else:
    #         print("%d年不是闰年" % year)
    #         return False
    #
    #
    # is_leap=[4,40,50,60,70,80,400,800,1996,2996]
    #
    # @pytest.fixture(params=is_leap)
    # def is_leap(self,request):
    #
    #     return request
    #
    # def test_is_leap(self,is_leap):
    #     assert self.is_leap_year(is_leap) == True

# import pytest
# class TestClass(object):
#     @pytest.fixture(params=[1, 2, 3, 4])
#     def test_result(self, add):
#         result = add
#         assert result == 8


if __name__ == "__main__":
    # pytest.main('-q demo.py')
    pytest.main()
