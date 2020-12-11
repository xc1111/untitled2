
class Game:
    def __init__(self,my_hp,your_hp ):
        self.my_hp = my_hp
        self.my_power = 200
        self.your_hp = your_hp
        self.your_power = 199

    def fight(self):
        # 对打多轮，血量小于等于0方者败
        while True:
            self.my_hp=self.my_hp-self.your_power
            self.your_hp=self.your_hp-self.my_power
            if self.my_hp<=0:
                print("我剩余血量为",self.my_hp)
                print("你剩余血量为",self.your_hp)
                print("我输了")
                break
            elif self.your_hp<=0:
                print("我剩余血量为",self.my_hp)
                print("你剩余血量为",self.your_hp)
                print("你输了")
                break
game=Game(2000,1000)
game.fight()

