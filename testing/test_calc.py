""""
1、补全计算器（加法 除法）的测试用例

2、使用参数化完成测试用例的自动生成

3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：

    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""

# 导入模块
import pytest
import yaml

from pythoncode.calc import Calculator

# 读取文件
with open('./datas/calc.yml') as f:
    # safe_load()只能一次
    data_source = yaml.safe_load(f)['div']
    # 获取数据
    mydatas = data_source['datas']
    print(mydatas)
    # 获取数据
    myid = data_source['myid']
    print(myid)

# 定义类
class TestCalc:
    # 定义setup_class()方法
    def setup_class(self):
        print("开始计算")
        # 实例化计算器
        self.calc = Calculator()

    # 定义teardown_class()方法
    def teardowm_class(self):
        print("结束计算")

    # 定义setup()方法
    def setup(self):
        print("要灵活使用")

    # 定义teardown()方法
    def teardowm(self):
        print("灵活使用结束")


    # 装饰器参数化  加法标记
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',[
        (1,1,2),
        (100,100,200),
        (0.1,0.1,0.2),
        (-1,-1,-2),
        ],ids=['int','bigint','float','minus'])
    # 定义一个test_add1()方法
    def test_add(self,a,b,expect):
        # 调用它的相加add()方法
         result=self.calc.add(a,b)
        # 判断result为小数的时候使用round取小数点后两位
         if isinstance(result,float):
             result=round(result,2)
        # 断言
         assert expect == result


    # 装饰器  yaml文件传入参数化
    @pytest.mark.div
    @pytest.mark.parametrize('a ,b,hope',mydatas,ids=myid)
    # 定义除法测试方法，传入参数和希望值
    def test_div(self,a,b,hope):
         # 除法结果
         result=self.calc.div(a,b)
         # 断言希望值是否等于除法结果
         assert hope == result




