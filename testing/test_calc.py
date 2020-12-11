# import pytest
# import yaml
#
# from pythoncode.calc import Calculator
#
# with open('./datas/calc.yml') as f:
#     data_source = yaml.safe_load(f)['div']
#     mydatas = data_source['datas']
#     print(mydatas)
#     myid = data_source['myid']
#     print(myid)
#
#
# class TestCalc:
#     def setup_class(self):
#         print("开始计算")
#         self.calc = Calculator()
#
#     def teardowm_class(self):
#         print("结束计算")
#
#     @pytest.mark.add
#     @pytest.mark.parametrize('a,b,expect',[
#         (1,1,2),
#         (100,100,200),
#         (0.1,0.1,0.2),
#         (-1,-1,-2),
#         ],ids=['int','bigint','float','minus'])
#     def test_add1(self,a,b,expect):
#          result=self.calc.add(a,b)
#          if isinstance(result,float):
#              result=round(result,2)
#          assert expect == result
#
#
#
#
#     @pytest.mark.div
#     @pytest.mark.parametrize('a ,b,hope',mydatas)
#     def test_add2(self,a,b,hope):
#          result=self.calc.div(a,b)
#          assert hope == result



