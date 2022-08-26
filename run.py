# coding:gbk
import pytest
import os
import subprocess
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


def init_env():
    cmd = "python3 -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python3 -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")


def init_report():
    cmd = "allure generate ./result/ -o ./reports/ --clean"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


# init_env()
# pytest.main(["-s", "testsuites", "--alluredir=./result/","--clean-alluredir"])
# pytest.main(["-s", "testsuites/test_host_close.py", "--alluredir=./result/","--clean-alluredir"])
# pytest.main(["-s", "testsuites_new", "--alluredir=./result/","--clean-alluredir"])
pytest.main(["-s", "testsuites_new/test_012_gift_send_graffiti.py", "--alluredir=./result/","--clean-alluredir"])
init_report()
