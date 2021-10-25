class HouseItem:
    """家具类"""
    def __init__(self, name, area):
        """初始化方法"""
        self.name = name
        self.area = area

    def __str__(self):
        """打印家具对象的描述"""
        return "家具名字：%s 占地面积：%.1f平米" % (self.name, self.area)


bed = HouseItem("席梦思", 4)
print(bed)

class House:
    """房子类"""
    def __init__(self, house_type, area):
        # 房子的户型
        self.house_type = house_type
        # 房子的总面积
        self.area = area
        # 房子的剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []


    def __str__(self):
        """打印房子对象的描述信息"""
        return "户型:%s, 总面积:%.1f平米。剩余面积:%.1f平米，家具名称列表:%s"\
            % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        """当前方法时添加家具的方法"""
        # item是家具对象的变量
        if self.free_area < item.area:
            print("添加%s 家具面积太大，无法添加！！！" % item.name)
            # 代码不再向下执行
            return
        # 更新房子的剩余面积
        self.free_area -= item.area
        # 把新添加的家具名称保存到 家具名称列表
        self.item_list.append(item.name)




my_house = House("大别墅", 200)
print(my_house)
# 添加一个bed
my_house.add_item(bed)
print(my_house)




