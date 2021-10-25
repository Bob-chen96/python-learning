聚合函数:count 返回总数
select count(*) as 男性人数 from students where gender = 1;

最大值: max()
查询最大年龄:
select max(age) from students;
最小值: min()
求和:sum()
平均值:avg ()
计算所有人的平均年龄,保留两位小数:
select round(avg (age), 2) from students;

分组: group by
select gender, count (*) from students group by gender;

group _concat(..)
select gender, group_concat(name, "_", age) from  students where gender = 1 group by gender;

having:和聚合一起使用
select gender, group_concat(name) from  students group by gender having avg(age)>30;
