# 各种导入类
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 定义测试TestDemo0类
class TestDemo0():

# 定义初始化method方法
    def setup_method(self,method):
# 选择好调试器地址
        option=Options()
        option.debugger_address='localhost:9222'
        self.driver=webdriver.Chrome(options=option)
        # self.driver=webdriver.chrome
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

# 定义初始化方法实现退出
    def teardown_method(self, method):
        self.driver.quit()

# 定义cookie测试类方法
    def test_cookie(self):
# 查看获取当前页面cookie给变量cookies：用get_cookies方法
        cookies=self.driver.get_cookies()
# 打印cookie，在结果端显示，复制到文本文件
        print(cookies)
# # 打开企业微信网页
#         self.driver.get("https://ceshiren.com/t/topic/5542")
# #粘贴所得到带有登录信息的cookie让临时变量cookies保存
#         cookies={[{'domain': '.ceshiren.com', 'httpOnly': False, 'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False, 'value': '1598102562'}, {'domain': 'ceshiren.com', 'expiry': 1603286553, 'httpOnly': True, 'name': '_t', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'd9bd7f8f72074db01929b44a5b9b3347'}, {'domain': '.ceshiren.com', 'expiry': 1598188954, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.613614723.1598075431'}, {'domain': '.ceshiren.com', 'expiry': 1598102614, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.ceshiren.com', 'expiry': 1629638561, 'httpOnly': False, 'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False, 'value': '1598075424,1598076847,1598100422,1598102562'}, {'domain': 'ceshiren.com', 'httpOnly': True, 'name': '_forum_session', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'KzZlekZ2bnkvN2YwM0FtTVdkS3FVakhsSzVuaWZaZ1c2RGVIRUVTYlNYalhMdUhRZUE0NVNPR0ZUUG1EVVNuTXVuRGVyNHUyZ0c5cndmNHNuTmp5T2N0TGx6L1BaYkRYS0p2UjJuYy83aHlmTzZ0K0xDQUNzUnE4aUg5L0NCUTZNTWZXdW0vVGhqUFRJL1JxeE0yQnYyTk90TlFmdGVkNGVPNlVuTFpjSm5HcHowM0pGUEp6QnJWc0habURsRkNoLS1rMkV1YlpRd0YwelJBZWN2V1ZsWUd3PT0%3D--2f8f3ae3eada6419c5021e09928a825a654f8be9'}, {'domain': '.ceshiren.com', 'expiry': 1661174554, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.872604365.1596502444'}]
#
#         }
# # 用for循环将cookies容器内数据一一取出遍历给cookie临时变量
#         for cookie in cookies:
# # 处理cookie中参数expiry的浮点数问题
#             if 'expiry' in cookie.keys():
#                 cookie.pop("expiry")
# # 把带有登录信息的cookie添加到页面上
#             self.driver.add_cookie(cookie)
# #重开带有cookie信息的index页面并强等3秒
#         self.driver.get("https://ceshiren.com/t/topic/5542")
#         sleep(3)
# # 下一段还不明白：与前段重复吗（应该是重复的。是个练习）
#
# # 定义importcontact测试方法
#     def Test_importcontact(self):
#
# # 打开企业微信网页网址：drive.get命令
#         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
# #粘贴所得到带有登录信息的cookie让临时变量cookies保存
#         cookies = []
#
# # 用for循环将cookies容器内数据一一取出遍历给cookie临时变量
#         for cookie in cookies:
#
# # 处理cookie中参数expiry的浮点数问题
#             if'expiry'in cookie.keys(https://work.weixin.qq.com/wework_admin/frame#index):
#                 cookie.pop("expiry")
#             self.driver.add_coolie(cookies)
# #重开带有cookie信息的index页面并强等3秒
#         self.driver.get()
#         sleep(2)
# # 找到导入联系人并点击
#         self.driver.find_element().click()
# # 通过定位找到上传并输入路径及类型
#         self.driver.find_element("").send_keys("")
# # 断言判断所查找到的文件名和路径是否正确。强等5秒
#         assert"mydata.xlsx"==self.drive.find_element().text
#         sleep(3)
# # 定义shelve测试方法（shelve=小型数据库）
# def shelve(self):
#
# # 创建数据库
#     db=shelve().open()
# # 将长串列表cookie放入创建的db变量名内
#     cookies=db['cookie']
# # ？
#
# # 将db内数据给cookies
#
# # 打开网页
#
# # 用for循环将cookies容器内数据一一取出遍历给cookie临时变量
#
# # 处理cookie中参数expiry的浮点数问题
#
# # 重开带有cookie信息的index页面并强等3秒
#
# # 找到导入联系人并点击
#
# # 通过定位找到上传并输入路径及类型
#
# # 断言判断所查找到的文件名和路径是否正确。强等5秒





