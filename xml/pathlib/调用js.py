import execjs


# 语句解析，open后跟所执行的js文件位置，call后第一个单引号引起来的为所执行的js文件的某个function，
# 第二个单引号是前面函数的参数
with open('1.js', 'r', encoding='utf-8') as f:
    jstext = f.read()

ctx = execjs.compile(jstext)
a = '1'
result = ctx.call('add', a)
print(result)


