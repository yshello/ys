class Music_Player(object):

    def __new__(cls, *args, **kwargs):

        # 1.创建对象时,new方法会被调用
        print("创建对象,分配空间")

        # 2.为对象分配空间
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):

        print("初始化对象")

player = Music_Player()
print(player)