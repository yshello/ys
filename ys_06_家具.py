class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "【%s】占地%.2f平方米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):

        return ("户型：%s\n 房间总面积：%.2f平方米 剩余：%.2f平方米\n 家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加家具%s" % item)
        # 1.判断家具面积是否大于剩余面积
        if item.area > self.free_area:
            print("%s 的面积太大" % item)
            return
        # 2.将家具的名称添加到列表
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area

# 1.创建家具
bed = HouseItem("席梦思床", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)

print(bed)
print(chest)
print(table)

# 2.创建房子
home = House("两室一厅", 100)
home.add_item(bed)
# home.add_item(chest)
# home.add_item(table)

print(home)
