# 定义基类
class Base:
    # 定义init方法和次数为空
    def __init__(self,number=None):
        # 如果次数为空
        if number is None:
            # 打印内容
            print("吃好，喝好，养精蓄锐，守米待鼠")
            # 否则
        else:
            # 次数定义给自己
            self.number=number
            # 打印内容
            print("主动出击，不发现老鼠就不休")
            # 实例化基类
base=Base()
