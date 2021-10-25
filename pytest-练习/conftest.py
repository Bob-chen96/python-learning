import pytest

"""
可以通过使用@pytest-练习.fixture注册成为一个fixture函数,来为测试用例提供一个Fixture函数
scope参数的可选值包括：function(函数),class(类),module(模块),package(包)及 session(会话)
"""
@pytest.fixture(scope="module")
def print_text():
    print("打印输出")


@pytest.fixture
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com",587,timeout=5)


