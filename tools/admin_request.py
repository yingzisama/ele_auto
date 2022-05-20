# coding:gbk
import requests
import json
import datetime

class AdminRequest:
    @staticmethod
    def login():
        url = 'http://showmetest-2011.elelive.cn:10009/login'
        data = {
            'smsCode':'1234',
            'userCode':'admin'
        }
        res = requests.post(url,data=data)
        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        (key, value), = cookie.items()
        new_cookie = key + '=' + value
        return new_cookie

    @staticmethod
    def get_feedback(cookie):
        url = 'http://showmetest-2011.elelive.cn:10009/user/feedback/list?page=1&size=10&userId=Test00026782&start=&end=&content=&problemTimeStart=&problemTimeEnd='
        header = {
            'Host':'showmetest-2011.elelive.cn:10009',
            'Referer':'http://showmetest-2011.elelive.cn:10009/main',
            'Cookie':cookie,
        }
        res = requests.get(url,headers = header)
        return json.loads(res.text)['items'][0]['createdDate']


if __name__=='__main__':
    cookie1 = AdminRequest.login()
    list_feed = AdminRequest.get_feedback(cookie1)
    print(type(list_feed))
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(type(now_time))
    
