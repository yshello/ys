class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 在地上玩耍" % self.name)


class XiaoTian(Dog):

    def game(self):
        print("%s 在天上玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def play(self, dog):
        print("%s 和 %s在玩耍" % (self.name, dog.name))


wangwang = Dog("旺旺")
xianming = Person("小明")
wangwang.game()
xianming.play(wangwang)