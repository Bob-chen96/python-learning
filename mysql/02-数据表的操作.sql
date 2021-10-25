查看当前数据库中所有表: show tables;

创建表: create table 表名 (字段名 类型 约束, ...);
查看表: desc 表名;

约束: auto_increment 自动增长  not null 不能为空
primary key 主键 default 默认值

1.创建students表:
create table students(
id int unsigned not null auto_increment primary key ,
name varchar(30),
age tinyint unsigned,
height decimal(5, 2),
gender enum("男", "女", "保密") default "保密",
cls_id int unsigned
);
insert into students values (0, "老王", 18, 180.88, "男", 1);