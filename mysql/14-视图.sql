视图: 一条select语句执行后返回的结果集,相当于一个虚拟表
修改数据库中的表时,视图会同步改变

创建视图: create view 视图名(建议以v_开头) as select 语句

查看视图:show tables;

使用视图: select * from 视图名;

删除视图:drop view 视图名;

视图的作用:对数据库重构,不影响程序的运行

