"""

    定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

    see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
    如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
    fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
    需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

    定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    加入模块化改造
"""


#定义类名Tonglao：类名首字母必须大写。形式：class 类名: 或 class 类名（父类名）:
class Tonglao:
    # 定义类属性且赋值。 在类体内，方法外的是类属性
    # hp=1000
    # 构造函数来构造另一钟属性：实例属性（位置在类内，方法内），顺带传参。形式：def __int__(self,属性名):
    def __init__(self,power,hp):
        # 实现楼上意义的固搭形式
        self.power=power
        self.hp=hp
    # 定义看见人的方法并传参数名字
    def see_pepple(self,name):
        # 如果名字等于无崖子
        if name=="wyz":
            # 打印内容
            print("师弟！！！！")
        #     否则名字等于李秋水
        elif name=="李秋水":
            # 打印内容
            print("呸，贱人")
            # 否则名字等于丁春秋
        elif name=="丁春秋":
            # 打印内容
            print("“叛徒！我杀了你”")

    # 定义天山折梅手方法
    def fight_zms(self,dr_hp,dr_power):
        # 爆发力会在武力值上提升十倍
        Power_burst=self.power*10
        # 童姥最后血量=敌人血量-童姥缩减一半血量
        finally_hp=dr_power-self.hp/2
        # 敌人最后血量=提升而来的爆发力-敌人血量
        dr_finally_hp=Power_burst-dr_hp
        # 如果童姥最后血量>敌人最后血量
        if finally_hp>dr_finally_hp:
            # 童姥赢
            print("童姥赢")
        # 如果童姥最后血量<敌人最后血量
        elif finally_hp<dr_finally_hp:
            # 童姥输
            print("童姥输")
        #     否则
        else:
            # 平局就抛出异常
            raise Exception("不要平局，平局就抛出异常")
  # 实例化童姥,传入武力和血量
tongLao=Tonglao(100,100)

# 调用见人方法
tongLao.see_pepple("wyz")

# 调用天山折梅手方法
tongLao.fight_zms(20,40)






