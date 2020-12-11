# 这是页面对象层！！
# po用类来表示页面对象
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_project.pages.main_page import Mainpage


class AddMemberpage(Mainpage):

    def __init__(self,driver):
        self.driver = driver
# 用方法去表现页面对象里面所使用的操作步骤
    def add_member(self):
        sleep(3)
        self.driver.find_element(By.ID,"username").send_keys("联系")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("3333")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13388881234")

        # return self
