模糊查询:
like:
% 替换一个或者多个
_替换1个
查询名字中有老所有名字:
select name, age from students where name like "%老%";

rlike 正则表达式
查询以老开头以王结尾的姓名:
select name from students where name rlike "^老.*王$";