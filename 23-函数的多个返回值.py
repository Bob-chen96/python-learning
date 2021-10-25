def mult_ex():
    tem = 27.5
    wetness = 89
    pm_25 = 120
    return [tem , wetness, pm_25]  # 返回多个数据，借助容器 列表，元组，字典

                                 #  不加括号返回元组类型
ret = mult_ex()
print(ret)
print(type(ret))