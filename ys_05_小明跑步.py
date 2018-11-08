class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "我叫%s,我的体重是 %.2f 千克" % (self.name, self.weight)

    def run(self):

        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):

        print("%s 是吃货，吃东西会变胖" % self.name)
        self.weight += 1

xiaoming = Person("小明", 70.5)

xiaoming.eat()
xiaoming.run()
print(xiaoming)
