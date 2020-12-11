import yaml
#

class Game:
    def __init__(self):
        data = yaml.safe_load(open("data2.yml"))
        print(data)
        self.my_skill = data["me"]["skill"]
        self.my_power =data["me"]["power"]
        self.my_hp = data["me"]["hp"]
        # print(self.my_hp )
        # print(self.my_hp)
#       print(self.my_hp )

        self.difficulty_skill=data["difficulty"]["skill"]
        self.difficulty_power =data["difficulty"]["power"]
        self.difficulty_hp =data["difficulty"]["hp"]



    def fight(self):
        # 对打多轮，血量小于等于0方者败
        while True:
            self.my_hp = self.difficulty_power - self.my_hp
            self.difficulty_hp = self.my_power*self.my_skill-self.difficulty_hp
            if self.my_hp <= 0:
                print("我剩余血量为", self.my_hp)
                print("困难剩余血量为", self.difficulty_hp)
                print("我输了")
                break
            elif self.difficulty_hp <= 0:
                print("我剩余血量为", self.my_hp)
                print("困难剩余血量为", self.difficulty_hp)
                print("困难输了")
                break
#
#
game = Game()
game.fight()