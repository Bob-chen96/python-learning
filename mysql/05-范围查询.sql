范围查询:
in(1, 3, 8) 表示在一个非连续的范围内
select name, age from students where age not in (12, 18,34);

between .. and .. 表示在一个连续的范围内

空判断:
判空: is null
判非空: is not null
