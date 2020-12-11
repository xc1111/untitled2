
# 这是业务逻辑层！！
# from test_project.pages.main_page import Mainpage
from test_project.pages.main_page import Mainpage


class TestAddmember(Mainpage):
    def test_add_member(self):
        # 初始化Main页面
        self.main=Mainpage().go_to_add_member()
        #  按照业务逻辑：1从首页跳转到添加成员页面2添加成员
        self.main.add_member()
        # .add_member().save_member()

    # def test_contact_member(self):
    #     self.main=Mainpage()
    #     # 按照业务逻辑：1从首页跳转到通讯录页面2跳转到添加成员页面3添加成员
    #     self.main.go_to_cotact().go_to_add_member().add_member()