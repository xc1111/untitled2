
    # 定义一个fight函数
def fight():
    my_hp=1000
    my_power=200
    your_hp=1000
    your_power=199
#     一轮对打
    my_final_hp=my_hp-your_power
    your_final_hp=your_hp-my_power
    if  my_final_hp>your_final_hp:
        print("我赢了")
    elif  my_final_hp<your_final_hp:
        print("你赢了")

#         调用fight函数
fight()


