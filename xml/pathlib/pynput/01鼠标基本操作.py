import time

from pynput import mouse

# 鼠标基本操作
# 获取鼠标操作对象
control = mouse.Controller()

# 获取当前鼠标位置
print(control.position)

# 改变鼠标位置
control.position = (100, 100)

time.sleep(1)
# 在原位上移动鼠标位置（x，y）
control.move(100, 100)

# 鼠标按键类型
# 左键 mouse.Button.left 右键：mouse.Button.right 中键：mouse.Button.middle

# 按下鼠标左键
control.press(mouse.Button.left)

# 双击鼠标左键,2为点击次数
control.click(mouse.Button.left, 2)

# 鼠标滚轮向上滚动
control.scroll(0, -100)

# 鼠标向下滑动
control.scroll(0, 100)