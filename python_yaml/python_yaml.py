# 打开yaml文件的练习
import yaml

class Game:
    def __init__(self):
        data=yaml.safe_load(open("data.yml"))
        print(data)

game=Game()