# -- coding: utf-8 --

# Author: Dongbob
# Team: DErsteller

import json
import os
from random import randint
from time import sleep


# API
class api:
    # 获取数据
    def getConfig(path):
        # current_path = os.path.dirname(__file__)
        with open(path + '.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data

    """ # 获取语言 """
    """ def getLang(): """
    """     lg = api.getData('settings')['lang'] """
    """     lang = api.getData("lang\\" + lg) """
    """     return lang """

    """ # 输入信息 """
    """ def msg(message): """
    """     print(api.getLang()[message]) """


# 游戏类
class game:
    # 退出程序
    def exit():
        print("炸弹数字为{}".format(num.bomb))
        print("退出中...")
        sleep(1)
        exit(0)

    # 跳过一回合
    def skip():
        print("炸弹数字为{}".format(num.bomb))
        print("跳过中...")
        sleep(0.5)

    # 玩家胜利
    def win():
        print("BOOM!")
        print("本局结束, 您获胜了!")
        sleep(1.5)

    # 玩家失败
    def lose():
        print("BOOM!")
        print("本局结束, 玩家{}胜利!".format(bot.name))
        sleep(1.5)

    # 欢迎语
    def welcome():
        print("欢迎游玩数字炸弹!")
        sleep(0.1)
        print("你将会和一名电脑玩家共同游玩!")
        sleep(0.1)
        print("系统会随机抽取已设定好的区间之内的整数,并由玩家竞猜")
        sleep(0.1)
        print("输入数字,系统将给出大小判断,若猜中则游戏结束")


# 数字类
class num:
    # 设定起始数字和结束数字
    start = 0
    end = 0
    # 初始化炸弹数字
    bomb = 0
    # 初始化玩家和电脑数字
    player = 0
    bot = 0
    # 初始化可取范围
    Snb = []
    Lnb = []

    # 设定开始和结束数字以及可取范围
    def setNumbers():
        namedict = api.getConfig('settings')
        num.start = namedict['start']
        num.end = namedict['end']
        num.Snb = [num.start]
        num.Lnb = [num.end]
        num.bomb = randint(num.start+1, num.end-1)


# 电脑玩家类
class bot:
    # 初始化名字
    name = "null"

    # 设置电脑玩家名字
    def setName():
        namedict = api.getConfig('settings')
        bot.name = namedict['name'][randint(0, len(namedict['name']) - 1)]


# 游戏玩家类
class player:
    # 初始化玩家输入
    input = "null"


game.welcome()
while True:
    # 电脑玩家名字随机设定
    bot.setName()
    # 设定数字
    num.setNumbers()
    sleep(0.5)
    print("匹配到电脑玩家 {}".format(bot.name))
    print("准备开始游戏!")
    sleep(0.5)
    # 开始游戏
    while True:
        # 获取玩家输入
        player.input = input("请输入{}到{}之间的整数:".format(
            max(num.Snb), min(num.Lnb)))
        # 判断是否为特定字符串
        if player.input == "exit":
            game.exit()
        elif player.input == "skip":
            game.skip()
            break
        else:
            try:
                # 判断是否有效,捕捉异常
                num.player = int(player.input)
            except ValueError:
                # 输出异常信息
                print("请输入有效的整数!")
            else:
                # 判定是否正确
                if num.player <= max(num.Snb):
                    print("请输入大于{}的整数".format(max(num.Snb)))
                    continue
                if num.player >= min(num.Lnb):
                    print("请输入小于{}的整数".format(min(num.Lnb)))
                    continue
                # 判定是否为炸弹数
                if num.player > num.bomb:
                    print("太大了!")
                    num.Lnb.append(num.player)
                elif num.player < num.bomb:
                    print("太小了!")
                    num.Snb.append(num.player)
                else:
                    game.lose()
                    break
                # 等待电脑输入
                sleep(0.1)
                print("等待对手{}输入...".format(bot.name))
                sleep(0.5)
                num.bot = randint(max(num.Snb) + 1, min(num.Lnb) - 1)
                sleep(randint(1, 3))
                print("玩家{}输入:{}".format(bot.name, num.bot))
                # 电脑判定
                if num.bot > num.bomb:
                    print("太大了!")
                    num.Lnb.append(num.bot)
                elif num.bot < num.bomb:
                    print("太小了!")
                    num.Snb.append(num.bot)
                else:
                    game.win()
                    break
    # 重新匹配
    print("重新匹配中...")
    sleep(0.5)
