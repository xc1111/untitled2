class Bicycle:
    def run(self,km):
        # 字面量插值传递Km参数
        print(f"骑行里程{km}km,好累好累呀")
# 再定义电动自行车类Ebicyle继承自Bicyle
class EBicycle(Bicycle):
    # 构造方法
    def __init__(self,valume):
        self.valume=valume
    #     def fill_charge(self,vol)表示用来充电，vol为电量

    def fill_charge(self,vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电后剩余{vol+self.valume}度")
    def run(self,km):
        # run(km)方法用于骑行，每骑行10km消耗电量1度
        # 电量耗尽时调用Bicyle的run方法骑行，通过传入的骑行里程数，显示骑行结果

        # 有电的时候能骑行的公里数
        e_km=self.valume*10
        print("电动车的最大公里数",e_km)

        # 当剩余电量能骑行的公里数大于行程
        if km-e_km<=0:
            print(f"用电一共骑了{km}km")
        else:
            # 用脚骑行公里数=总公里数-用电的公里数
            print(f"用电一共骑了{e_km}km")
            # 调用父类的方法
            super().run(km-e_km)
            print(f"手动骑了{km-e_km}km")
#

# 继承之后子类可调用父类属性和方法
# 构造方法（函数）的参数时，需要在实例化类（调用函数）时候就设好实参才可以有参数传递
ebike=EBicycle(100)
ebike.run(10000)
ebike.fill_charge(10)

# 类在实例化的时候需要加刮号
bike=Bicycle()
bike.run(100)