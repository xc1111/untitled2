# po用类来表示页面对象
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_project.pages.contact_page import Contactpage
from selenium import webdriver

class Mainpage:
    def go_to_add_member(self):
        from test_project.pages.add_member_page import AddMemberpage
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)
        self.driver.find_element(By.XPATH,'//*[@node-type="addmember"]').click()
        return AddMemberpage(self.driver)
