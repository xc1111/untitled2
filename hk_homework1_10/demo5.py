# 导入基类
from hk_homework1_10.demo6 import Base

# 定义猫类
class Cat(Base):
    # 定义去抓老鼠方法
    def go_to_mouse(self):
        # 返回基类，能拿到父类属性，因为继承
        return Base(self.number)
# 实例化红猫
redcat=Cat()

# from hk_demo.demo3 import Cat
# from hk_demo.demo4 import Rice
#
#
#
# number_one=Rice('一',20)
# print(number_one)
#
# number_two=Rice('二',30)
# print(number_two)
#
# number_three=Rice('三',40)
# print(number_three)
#
# # class Mouse(Cat):
# #     def __init__(self):
# #         self.weight = []
# #
# #         super().__init__("老鼠","黑不溜秋",0.5)
# #
# #     def __str__(self):
# #         return
#


# redcat.go_to_mouse()

