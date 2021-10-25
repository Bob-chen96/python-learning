创建账号: grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
如: grant select on pytest.* to 'Bob2'@'localhost' identified by '123456';
表示创建一个新账号,对pytest库所有的列表有查询权限
grant all privileges on ... 表示拥有所有权限