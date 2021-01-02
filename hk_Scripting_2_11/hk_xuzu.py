# 导入童姥模块
from hk_Scripting_2_11.hk_tonglao import Tonglao

# 定义虚足类
class Xuzhu(Tonglao):


    # 定义念经方法
    def read(self):
        # 打印内容
        print("罪过罪过")

    # super().fight_zms(1000,100) 有重写同名的天山折梅手方法，同时又需要调用父类的天山折梅手方法时可用
# 实例化虚足
zxrh=Xuzhu(100,100)
# 调用念经方法
zxrh.read()
# zxrh.fight_zms(100,100)

