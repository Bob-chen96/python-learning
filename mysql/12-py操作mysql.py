from pymysql import *

# 创建connection连接
conn = connect(host='localhost', port=3306, user='root', password='love19967410', database='pytest-练习', charset='utf8')

# 获得Cursor对象
csl = conn.cursor()

# 执行select语句,返回受影响的行数
line = csl.execute('select * from students;')
print(line)

# 获取一条数据,返回一个元组
line_content = csl.fetchone()
print(line_content)

# 获取所有数据,只会获取剩下的
lines_content = csl.fetchall()
print(lines_content)

# 关闭Cursor对象
csl.close()
conn.close()

