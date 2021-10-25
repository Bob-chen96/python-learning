def input_pwd():
    pwd = input("请输入密码：")
    if len(pwd) < 8:
        print("抛出异常")
        # 使用Exception类创建对象 Exception（错误提示）
        ex = Exception("错误：密码长度小于8位")
        # 使用raise抛出异常对象
        raise ex
    else:
        return pwd


# input_pwd()

try:
    ret = input_pwd()
    print(ret)
except Exception as exp:
    print("捕获异常信息，exp：", exp)