# coding:gbk
import requests
import pymysql
import json
import redis

userId = '11839791'

class ele_function:
    @staticmethod
    def login():
        now_host = 'http://showmetest3.elelive.cn:10009'
        url = now_host+'/login'
        data = {
        'smsCode':'1234',
        'userCode':'Fish'
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

    @staticmethod
    def grow_clear():
        '''����û���11839791��õ��ɳ���������ݿ��redis����'''
        #���ݿ�
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
        db1.execute("delete FROM account.user_gift_grows_info where user_id = '11839791'")
        count.commit()

        # ����redis
        r = redis.StrictRedis(host='47.112.74.18',port=30013,password='showmeTEST_3318',db=0,decode_responses=True)
        # ɾ��key������
        r.delete("USER_GIFT_GROWABLE_ENABLE_11839791_202")
        # print(r.smembers('USER_GIFT_GROWABLE_11839791_202'))
        r.delete("USER_GIFT_GROWABLE_11839791_202")
        # print(r.hgetall("USER_GIFT_GROWABLE_11839791_202"))

    @staticmethod
    def fans_clear():
        '''����û���˿���'''
        #���ݿ�
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
        db1.execute("delete FROM fansclub.cmedal_info where user_id = '11839791'")
        db1.execute("delete FROM fansclub.exp_record_info WHERE user_id = '11839791'")
        db1.execute("delete FROM  fansclub.fans_joint_history_record_info WHERE user_id = '11839791'")
        count.commit()

        r = redis.StrictRedis(host='47.112.74.18',port=30013,password='showmeTEST_3318',db=0,decode_responses=True)
        r.delete("FANS_EXP_CLUB_12229221")


if __name__=='__main__':
    ele_function.grow_clear()
    
