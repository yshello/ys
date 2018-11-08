class Cat:

    def eat(self):
        print("%s吃鱼" % self.name)

    def drink(self):
        print("%s喝水" % self.name)

# 创建猫对象
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()

print(tom)

# 创建另一个猫对象
lay_cat = Cat()
lay_cat.name = '大懒猫'
lay_cat.eat()
lay_cat.drink()

print(lay_cat)