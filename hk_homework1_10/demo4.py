# 导入基类
from hk_homework1_10.demo6 import Base
# 定义大米类,继承基类
class Rice(Base):
    #定义str方法
    def __str__(self):
        # return print(f"因为被吃第{self.number}次,吃了{self.g}")
        # 返回打印内容
        return print(f"因为被吃第5次,吃了50g")
# 实例化稻花香
daohuaxiang = Rice()
# 打印它
print("daohuaxiang")

    # def eat(self, number, g):
    #     self.g = g
    #     self.number = number
    #     print(f"被吃第{self.number}次,吃了{self.g}")






