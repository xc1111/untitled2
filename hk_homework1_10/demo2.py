# 定义猫类
class Cat:
    # 构造函数初始化：初始化同时设置初始值姓名和颜色，体重
    def __init__(self,name,color,weight):
        # 形参姓名保存为属性
        self.name=name
        # 形参颜色保存为属性
        self.color=color
        # 形参体重保存为属性
        self.weight=weight

    # 定义str方法：当输出对象时可不输出地址而是自定义的内容
    def __str__(self):
            # return "我的名字叫 %s 颜色是 %s  " % (self.name, self.color)
            # 返回打印内容
            return print(f"我的名字叫{self.name},我肤色是{self.color},我体重是{self.weight}")

    # 定义捕捉方法
    def catch(self):
        # 设置判断条件
        if self.weight<5 or self.weight ==5:
            # 条件成立，执行代码：打印内容
            print('抓不到老鼠')
            # 否则，当条件2成立
        elif self.weight==6:
            # 执行此代码：打印此内容
            print('可以试试看')
            # 那一个条件成立
        else:
            # 执行此代码，打印内容
            print("抓到老鼠了")
# 类模板创建对象 第二只猫，传入名字，颜色，体重的实参
twocat=Cat("白猫","白色",5.5)
# 调用对象捕捉方法
twocat.catch()
# 打印对象 第二只猫
print(twocat)
