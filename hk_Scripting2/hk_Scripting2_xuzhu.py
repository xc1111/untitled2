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
    # 定义了类名的一个方法（看特征有无self，函数可以没有self），同时顺带先铺垫下等下就传参。形式：def 方法名(self,参数名):
    def see_pepple(self,name):
        # 是参数不传参数值，走个过场形式还是要的，不然没存在感

        if name=="wyz":
            print("师弟！！！！")
        elif name=="李秋水":
            print("呸，贱人")
        elif name=="丁春秋":
            print("“叛徒！我杀了你”")

    def fight_zms(self,dr_hp,dr_power):
        Power_burst=self.power*10
        finally_hp=dr_power-self.hp/2
        dr_finally_hp=Power_burst-dr_hp
        if finally_hp>dr_finally_hp:
            print("童姥赢")
        elif finally_hp<dr_finally_hp:
            print("童姥输")
        else:
            raise Exception("不要平局，平局就抛出异常")
tongLao=Tonglao(100,100)
Tonglao.fight_zms()

class Xuzhu(Tonglao):
    def read(self):
        print("罪过罪过")
    super().fight_zms(1000,100)

zxrh=Xuzhu()
Xuzhu.read()



