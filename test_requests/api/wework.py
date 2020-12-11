import requests
class Wework:
    def get_token(self):
        corpid = "wwcff06abedc04ea12"
        corpsecret = "841VLtxqhkCw4YxlOqqR2_wwCn2_hABngHM_OUgxzjI"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        return r.json()["access_token"]