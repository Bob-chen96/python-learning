class Gun:
    """枪支类"""
    def __init__(self, type):
        # 枪支类型
        self.type = type
        # 子弹数量 默认是
        self.bullet_count = 0

    def add_bullet(self, count):
        """添加子弹的方法"""
        self.bullet_count += count

    def shoot(self):
        """射击方法"""
        # 先判断枪支有没有子弹
        if self.bullet_count <=0:
            print("还没有子弹，不能射击，请先添加子弹！！")
            # 代码不再向下运行
            return

        self.bullet_count -= 1
        print("剩余子弹数量：%d" % self.bullet_count)


# ak47 = Gun("ak47")
# ak47.add_bullet(10)
# ak47.shoot()

class Soldier:
    """士兵类"""
    # gun = None 缺省参数，有默认值
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun == None:
            print("当前士兵：%s 还没有枪，不能开火，请分配枪支！" % self.name)
            return

        self.gun.shoot()


ak47 = Gun("AK47")
# 一个类中的对象可以作为另一个类中对象的参数
ak47.add_bullet(50)
xsd = Soldier("许三多", ak47)
xsd.fire()
xsd.fire()
