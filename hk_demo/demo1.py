# 定义猫类
class Cat:
    # 构造函数初始化：初始化同时设置初始值姓名和颜色
    def __init__(self,name,color):
        # 形参姓名保存为属性
        self.name=name
        # 形参颜色保存为属性
        self.color=color
# 定义捕捉方法
    def catch(self):
        # 打印
        print(f"抓到老鼠了")
# 定义str方法：当输出对象时可不输出地址而是自定义的内容
    def __str__(self):
        # return "我的名字叫 %s 颜色是 %s  " % (self.name, self.color)
        # 返回打印内容
        return  print(f"我的名字叫{self.name},我肤色是{self.color}")
        # return print ('my name is {}, color is {}'.format(self.name,self.color))
# 类模板创建对象 第一只猫，传入名字和颜色的实参
onecat=Cat("黑猫","黑色")
# 调用对象捕捉方法
onecat.catch()
# 打印对象 第一只猫
print(onecat)
# 就是打印结果可正常显示但还会报错不知道何原因，如何改？？？