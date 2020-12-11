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
            # 返回打印内容
            return "我的名字叫 %s 颜色是 %s 体重是%.2f" % (self.name, self.color,self.weight)
            # return print(f"我的名字叫{self.name},我肤色是{self.color},我体重是{self.weight}")
    # 定义捕捉方法,方法里传入次数参数
    def catch(self,time):
       # 设置循环,再设置循环条件
        while time<3:
            # 控制循环条件
            time+=1
            # 嵌套个永久循环,
            while True:
                # 打印内容
                print(('等着老鼠被抓到'))
                # 灵活结束永久循环
                break
# 类模板创建对象 第三只猫，传入名字，颜色，体重的实参
threecat=Cat("波斯猫","波斯色",5.555)
# 调用对象捕捉方法,传入次数的实参
threecat.catch(0)
# 打印对象 第三只猫
print(threecat)