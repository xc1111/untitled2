import requests
class Label:

    def create_label(self,token,label_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        data = {"tagname": "坚持",
                "tagid": label_id}
        r = requests.post(url=create_url, json=data)
        return r.json()

    def update_label(self,token,id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        data = {
            "tagid":id,
            "tagname": "坚持就是胜利"
        }
        r = requests.post(url=update_url, json=data)
        return r.json()

    def delate_label(self,token,label_id):
        delete_label_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={label_id}"
        r = requests.get(url=delete_label_url)
        return r.json()

    def get_label_list(self,token):
        get_laber_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        list = requests.get(url=get_laber_list_url)
        return list
