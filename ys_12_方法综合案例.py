class Game(object):

    # 历史最高分
    top_score = 999

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("敌军还有30s到达战场,请准备")

    @classmethod
    def show_top_score(cls):
        print("游戏的最高分为：%d" % cls.top_score)

    def start_game(self):
        print("%s 欢迎来到英雄联盟" % self.player_name)

# 1.显示提示信息
Game.show_help()

# 2.显示历史最高分
Game.show_top_score()

# 3.欢迎玩家进入
xiaoming = Game("小明")
xiaoming.start_game()