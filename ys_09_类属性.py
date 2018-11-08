class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具数量
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

tool1 = Tool("锤子")
tool2 = Tool("斧头")
print(Tool.count)