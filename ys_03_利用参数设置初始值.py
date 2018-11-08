class Cat:

    def __init__(self, new_name):
        self.name = new_name

    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)

# 使用类名（）创建对象的时候，会自动调用__init__方法
# 创建猫对象
tom = Cat("Tom")

tom.eat()
tom.drink()


# 创建另一个猫对象
lay_cat = Cat("懒猫")

lay_cat.eat()
lay_cat.drink()
