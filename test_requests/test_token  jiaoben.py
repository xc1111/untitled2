
import requests
class TestToken:
    def test_get_token(self):
        corpid="wwcff06abedc04ea12"
        corpsecret="841VLtxqhkCw4YxlOqqR26v0foTCt6YXgRIjnn9JW74"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.json())


