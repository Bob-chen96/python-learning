def input_plus(msg):
    """
    当前函数对input函数进行功能扩充
    :return:
    """
    #  1.使用input函数获取用户信息
    info = input(msg)
    #  2.对输入信息进行判断
    if len(msg) > 0:
        return info
    else:
        return
