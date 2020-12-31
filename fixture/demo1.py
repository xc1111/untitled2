import pytest

#创建一个登录的fixture方法
@pytest.fixture()
def login():
    print("完成登录操作")
    print("获取token")

#测试用例1 :需要提前登录
def test_case1(login):
    print("测试用例1")

#测试用例2 ：不需要提前登录
def test_case2():
    print("测试用例2")

#测试用例3 :需要提前登录
def test_case3(login):
    print ("测试用例3")
