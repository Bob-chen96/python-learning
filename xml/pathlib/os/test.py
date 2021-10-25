import os
import sys
from pathlib import Path

# os.chdir(r"D:\suwell-wps\suwell4\config")
# path = Path(r"D:\suwell-wps\suwell4\config")
# print(path)
# from path.const import Const
sys.path.append(r"D:\suwell-wps\suwell4")
from config.const import Const
print(Const.TEST_EXE_PATH)

