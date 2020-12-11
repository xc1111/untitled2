from test_requests.api.label import Label
from test_requests.api.wework import Wework


class TestLabel(object):
    def setup_class(self):
        wework=Wework()
        self.token=wework.get_token()
        self.label= Label()

    def test_create_label(self):
        self.label.create_label(self.token,12)
        list=self.label.get_label_list(self.token)
        assert list.json()["taglist"][1]["tagname"] == '坚持'


    def test_update_label(self):
        self.label.update_label(self.token,12)
        list = self.label.get_label_list(self.token)
        assert list.json()["taglist"][1]["tagname"] == '坚持就是胜利'


    def test_delate_label(self):
        self.label.delate_label(self.token,12)
        list = self.label.get_label_list(self.token)
        assert len(list.json()["taglist"]) == 1


    def test_get_label_list(self):
        self.label.get_label_list(self.token)


