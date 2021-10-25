import pytest


class TestClass(object):
    def test_fun(self, print_text):
        assert 3 == 5

    # @pytest-练习.mark.slow
    def test_name(self, print_text):
        assert "cc" in "Bob_cc"


"""
1.pytest-练习 test_01.py::TestClass::test_fun 执行单个用例

2.创建JUnit XML格式的测试报告#
要创建可由Jenkins或其他持续集成软件读取的XML测试报告,可以使用
pytest-练习 --junitxml=path(xml生成路径）
生成测试报告：allure generate xml路径 测试报告路径
"""
