修改表-添加字段：alter table 表名 add 字段名 类型;
alter table students add birthday datetime;

修改表-修改字段（不重命名）：alter table 表名 modify 字段名 类型及约束
alter table students modify birthday date default '1999-01-01';

修改表-修改字段（重命名）：alter table 表名 change 原字段名 新名 类型及约束;
alter table students change birthday birth date default "2020-01-01";

修改表-删除字段：alter table 表名 drop 字段名
alter table students drop birth;

删除表：drop table 表名;
删除数据库：drop database 数据库名;

增：insert into 表名 values (, , ,);
或者 insert into 表名（字段1，字段2）values （1,2）;

改：update 表名 set 字段名1=1 , 字段名2=2 where ...;

删：delete from 表名 where..;

用as为字段名指定别名
select 字段 as 新字段名，字段2 as 字段名2 from 表名
select name as 姓名,gender as 性别 from students;