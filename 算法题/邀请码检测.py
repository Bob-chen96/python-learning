def verify_code(code):
    """假设这里的code定义是十六位字符串"""
    # 建立对应关系
    dic = dict()
    num = 1
    for alpha in "abcdefghijklmnopqrstuvwxyz":
        if num > 9:
            num = 1
        dic[alpha] = num
        num += 1

    _temp_list = list(code)[::-1]  # 逆向列表
    odd = 0
    even = 0
    for index, v in enumerate(_temp_list):
        index += 1
        if index % 2:
            # 奇数位处理
            if v.isalpha():
                _num = dic[v]
                odd += _num
                continue
            odd += int(v)
        else:
            # 偶数位处理
            if v.isalpha():
                _num = (dic[v]) * 2
                if _num > 9:
                    even += (_num - 9)
                    continue
                even += _num
                continue
            _num = int(v) * 2
            if _num > 9:
                even += (_num - 9)
                continue
            even += int(v)
    # 验证结果
    if (odd + even) % 10:
        print("error")
    else:
        print("ok")


