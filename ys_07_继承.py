class Anmail:

    def eat(self):
        print("吃东西")

    def drink(self):
        print("喝水")

    def sleep(self):
        print("睡觉")


class Dog(Anmail):

    def dark(self):
        print("我会狗叫")


class XiaoTian(Dog):

    def fly(self):
        print("我会飞")

    def dark(self):

        # 1.针对子类特有的需求重载方法
        print("我会说话")
        # 2.使用super(),调用原本在父类封装的方法
        super().dark()
        # 3.增加其他子类的代码
        print("@#$%$^%$#$%$^$")


xtq = XiaoTian()
xtq.fly()
xtq.drink()
xtq.dark()
