
import requests
class TestLabel:
    def setup(self):
        corpid="wwcff06abedc04ea12"
        corpsecret="841VLtxqhkCw4YxlOqqR2_wwCn2_hABngHM_OUgxzjI"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        # print(r.json())
        self.token = r.json()["access_token"]
        self.id=12

    def test_create_label(self):
        create_url=f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {"tagname": "坚持",
                "tagid": self.id}
        r = requests.post(url=create_url,json=data)
        print(r.json())
        assert r.json()["errmsg"] == 'created'
        # 调用获取标签成员接口去验证创建标签接口是否真创建成功
        get_laber_list_url=f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        list= requests.get(url=get_laber_list_url)
        print(list.json())
        assert list.json()["taglist"][1]["tagname"]== '坚持'
        assert r.json()["errmsg"] == 'created'

    def test_update_label(self):
        update_url=f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": self.id,
            "tagname": "坚持就是胜利"
        }
        r = requests.post(url=update_url, json=data)
        print(r.json())
        assert r.json()["errmsg"] == 'updated'
        get_laber_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        list = requests.get(url=get_laber_list_url)
        print(list.json())
        assert list.json()["taglist"][1]["tagname"]== '坚持就是胜利'
        assert r.json()["errmsg"] == 'updated'

    def test_delete_label(self):
        delete_label_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={self.id}"
        r = requests.get(url=delete_label_url)
        print(r.json())
        assert r.json()["errmsg"] == 'deleted'
        get_laber_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        list = requests.get(url=get_laber_list_url)
        print(list.json())
        # 发现视频里更新部门时id会缩短一半，所以删除部门时就获取其id长度来验证。那我获取标签列表不获取其id长度，直接这样按里面信息断言不建议吗？？？代码现在先注释掉了
        # assert list.json()["taglist"][0]["tagid"]== 1
        assert len(list.json()["taglist"]) == 1
        assert r.json()["errmsg"] == 'deleted'
