# coding:gbk
import requests
import pymysql

class ele_function:
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
    def add_coin(ele_coin):
        count = pymysql.connect(
        host = 'mysqltest3.elelive.cn',     
        port = 10634,        
        user='showmetest_app',        
        password='M90JB123kdF95',     
        db= '',  
        charset = 'gbk'     
        )
        count.ping(reconnect = True)
        # ���mysql���ݿ�ʵ����
        db1 = count.cursor()
        userId = 'Test12230543'
        db1.execute("update account.wallet_info set contributions_balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        count.commit()
        # ������������
        # db1.execute("SELECT user_id, contributions_balance FROM account.wallet_info where user_id = '%s'" % (userId))
        # result = db1.fetchone()
        # print(result)

    @staticmethod
    def add_bean(ele_coin):
        count = pymysql.connect(
        host = 'mysqltest3.elelive.cn',     
        port = 10634,        
        user='showmetest_app',        
        password='M90JB123kdF95',     
        db= '',  
        charset = 'gbk'     
        )
        userId = 'Test12230543'
        count.ping(reconnect = True)
        # ���mysql���ݿ�ʵ����
        db1 = count.cursor()
        db1.execute("update wallet.wallet_0 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_1 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_2 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_3 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_4 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_5 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_6 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_7 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_8 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_9 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        count.commit()

if __name__=='__main__':
    ele_function.add_bean(67)
    