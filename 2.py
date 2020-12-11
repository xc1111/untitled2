print("hello")
    # 定义一个fight函数
def fight():
    # 定义四个变量，存放俩角色各自的血量和攻击力
    my_hp=1000
    my_power=200
    your_hp=1000
    your_power=199
#     对打一轮
    my_final_hp=my_hp-your_power
    your_final_hp=your_hp-my_power
    if  my_final_hp>your_final_hp:
        print("我赢了")
    elif  my_final_hp<your_final_hp:
        print("你赢了")
    else:
        print("平局")

#         调用fight函数
fight()
