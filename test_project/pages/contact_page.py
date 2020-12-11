# po用类来表示页面对象
class Contactpage:
# 用方法去表现页面对象里面所使用的操作步骤
#     点击添加通讯录
    def go_to_add_member(self):
        # 解决循环导入问题
        from test_project.pages.add_member_page import AddMemberpage
        return AddMemberpage()
    # 点击添加成员
