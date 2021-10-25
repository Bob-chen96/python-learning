import tkinter as tk
from tkinter.messagebox import showerror

# 实例化窗口
w = tk.Tk()


def exit():
    global w
    w.destroy()
    w.quit()


def confirm():
    # 字符串类型
    page = page_num.get()
    time = running_time.get()
    if len(page) > 0 and len(time) > 0:
        # 判断输入是否是正整数
        if page.isdigit() and time.isdigit():
            w.quit()
            return page, time

        else:
            showerror(title="参数错误", message="参数类型不正确，请输入正确数字")
            return False
    else:
        showerror(title="参数错误", message='输入的参数不能为空')
        return False
    exit()

def start_run():
    # 窗口可视化名字
    w.title("My Window")

    # 设置窗口大小，乘是小x
    w.geometry('350x140')
    w.wm_attributes('-topmost', 1)

    # 在图形界面上设置标签
    tk.Label(w, text="文件页数:",  width="15", height="2").grid(row=0, column=0, stick=tk.W)
    tk.Label(w, text="执行时间(s)",  width="15", height="2").grid(row=1, column=0, stick=tk.W)

    # 在图形上设定输入框控件entry
    global page_num, running_time
    page_num = tk.Entry(w, show=None, bg="white", width="15")
    page_num.grid(row=0, column=1, stick=tk.W)
    running_time = tk.Entry(w, show=None, bg="white", width="15")
    running_time.grid(row=1, column=1, stick=tk.W)

    # 设定按钮，command=函数名，点击调用该函数
    tk.Button(w, text="确认", width="10", height="1", command=confirm).grid(row=10, column=1, stick=tk.W)

    # # pack用来放置标签，自动调节尺寸
    # b.pack()

    # 主窗口循环
    w.mainloop()


if __name__ == "__main__":
    start_run()
    print(confirm())
    exit()
    # print(a[0])
    # print(int(a[1]))
