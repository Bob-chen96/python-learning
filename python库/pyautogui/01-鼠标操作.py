import pyautogui

"""获取屏幕分辩率"""
size = pyautogui.size()
print(size)  # Size(width=1920, height=1080)
print(type(size))  # <class 'pyautogui.Size'>
print(size.height)  # 1080

"""移动鼠标"""
# 将鼠标移动到指定的坐标；duration 的作用是设置移动时间
pyautogui.moveTo(100, 100, duration=1)
#
# # 鼠标当前位置向右移动100px，向下移动500px, 这个过程持续 1 秒钟；
pyautogui.moveRel(100, 500, duration=2)

# 获取鼠标位置
position = pyautogui.position()
print(type(position))  # <class 'pyautogui.Point'>
print(position)  # Point(x=205, y=598)
print(position.x)

"""控制鼠标点击"""
# 单击鼠标,button 有left,middle,right
pyautogui.click(500, 500, button='left', clicks=5, interval=1)

# 双击鼠标
pyautogui.doubleClick(100, 100)  # 指定位置，双击左键
pyautogui.rightClick(100, 100)  # 指定位置，双击右键
pyautogui.middleClick(100, 100)  # 指定位置，双击中键

# 点击 释放
pyautogui.mouseDown()  # 鼠标放下
pyautogui.mouseUp()  # 鼠标释放

"""控制鼠标拖动"""
# 拖动到指定位置
pyautogui.dragTo(100, 300, duration=1)

# 按方向拖动 向右拖动100px，向下拖动500px
pyautogui.dragRel(100, 500, duration=1)

# 控制鼠标滚动
pyautogui.scroll(300)
