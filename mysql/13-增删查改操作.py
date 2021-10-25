from pymysql import *

# 创建connection连接
conn = connect(host='localhost', port=3306, user='root', password='love19967410', database='pytest-练习', charset='utf8')

# 获得Cursor对象
csl = conn.cursor()

# 增删改语句
count = csl.execute("update students set age = 20 where cls_id = 1;")
# 打印影响的行数
print(count)

# 和查不同之处是，增删改必须添加commit语句后，才会执行语句
conn.commit()

# 关闭Cursor对象
csl.close()
conn.close()
