import pyautogui
from pathlib import Path

"""获取屏幕截图"""
# 返回屏幕的截图，是一个Pillow的image对象
pic = pyautogui.screenshot()
print(pic)  # <PIL.Image.Image image mode=RGB size=1920x1080 at 0x2376EB01CD0>
pic.save(Path(__file__).absolute().parent.joinpath("截屏.png"))

#  返回im对象上，（500，500）这一点像素的颜色，是一个RGB元组
pix = pic.getpixel((500, 500))  # (43, 43, 43)
print(pix)

"""识别图像"""
btm = pyautogui.locateOnScreen('截图.png')
print(btm)

pyautogui.alert()

