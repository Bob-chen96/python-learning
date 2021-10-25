连接查询:
内连接 inner join .. on  取两个表都有的数据
select * from students inner join classes on students.cls_id = classes.id;(显示两个表的所有字段)
select s.*, c.name from students as s inner join classes as c on s.cls_id = c.id;(显示所选字段)

左连接: left join .. on 以左边的表为基准
select * from students as s left join classes as c on s.cls_id = c.id;

有连接 right join .. on
