from hk_demo.demo7_me import me


class Frustration:
    def __init__(self,hp,power,skill):
        self.hp=hp
        self.power=power
        self.skill=skill
    # def __str__(self):
    #     print(f"敌人的血量是{self.hp},力量是{self.power},潜力可将攻击力释放{self.skill}倍")
work_frustration=Frustration(100,80,0)
# print(work_frustration)

class Game:
    def fight(self):
        print(me.self.hp)
        while True:
            me.self.hp=work_frustration.power-me.self.hp
            work_frustration.hp=me.self.power-work_frustration.hp
            if me.self.hp==0:
                print("挫折赢了")
            else:
                print("我赢了")

game=Game()
game.fight()