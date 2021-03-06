from pynput import mouse

# 鼠标move监听
def on_move(x, y):
    print(f'Current position： ({x}, {y})')


# 鼠标click监听
def on_click(x, y, button, pressed):
    print(f'Click position： ({x}, {y})')
    print(f'Click button： {button}')
    print(f'Click state: {"Pressed" if pressed else "Release"}')


# 鼠标滚轮scroll监听
def on_scroll(x, y, dx, dy):
    print(f'Scroll position： ({x}, {y})')
    print(f'Scroll direction： ({dx}, {dy})')


with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()