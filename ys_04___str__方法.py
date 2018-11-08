class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s 我来了" % self.name)

    def __str__(self):
        return "我是小猫%s" % self.name

    def __del__(self):
        print("%s 我走了" % self.name)

# 使用类名（）创建对象的时候，会自动调用__init__方法
# 创建猫对象
tom = Cat("Tom")
print(tom)