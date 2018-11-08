class Music_Player(object):

    # 定义一个类属性，记录第一个被创建对象的引用
    instance = None
    # 定义一个类属性，记录是否执行初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否为空对象
        if cls.instance is None:
            # 2.调用父类的方法，为对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保留的对象引用
        return cls.instance

    def __init__(self):

        # 1.判断是否执行过初始化操作
        if Music_Player.init_flag:
            return
        # 2.如果没有执行过，执行初始化操作
        print("播放器初始化")
        # 3.修改类属性标记
        Music_Player.init_flag = True

player1 = Music_Player()
print(player1)

player2 = Music_Player()
print(player2)