import pytest

"""
@pytest.mark.parametrize允许在测试函数或类中定义多组参数和Fixture
"""


class TestClass(object):
    # 两组参数相当于两条用例
    @pytest.mark.parametrize("test_input, result", [["6*6", 36], ["6+9", 14]])
    def test_example(self, test_input, result):
        assert eval(test_input) == result


