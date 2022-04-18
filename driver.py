# coding:gbk
import uiautomator2 as u2
import os
from config import *
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


class Driver():
    def init_driver(self,device_name):
        try:
            logger.info(device_name)
            d = u2.connect(device_name)
            d.implicitly_wait(wait_timeout)
            logger.info("连接设备:{}".format(device_name))
            return d
        except Exception as e:
            logger.info("初始化driver异常!{}".format(e))
