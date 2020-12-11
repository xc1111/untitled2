from game.python_game import Game


class HouYi( Game):
    def __init__(self):
        # 继承父类的构造方法
        super().__init__(1000,1000)
        self.defense=100
    def fight(self):
            # 对打多轮，血量小于等于0方者败
            while True:
                self.my_hp = self.my_hp+self.defense - self.your_power
                self.your_hp = self.your_hp - self.my_power
                if self.my_hp <= 0:
                    print("后裔剩余血量为", self.my_hp)
                    print("你剩余血量为", self.your_hp)
                    print("我输了")
                    break
                elif self.your_hp <= 0:
                    print("后裔剩余血量为", self.my_hp)
                    print("你剩余血量为", self.your_hp)
                    print("你输了")
                    break


houyi=HouYi()
houyi.fight()

