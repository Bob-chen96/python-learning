import pytest

"""
tmp_path 在临时目录根目录中创建一个独立的临时目录以供测试调用。

tmp_path是一个pathlib/pathlib2.Path对象
"""


class TestClass(object):

    def test_create_file(self, tmp_path):
        # C:\Users\86189\AppData\Local\Temp\pytest-of-86189\pytest-2160\test_create_file0
        print(tmp_path)
        print(type(tmp_path))


