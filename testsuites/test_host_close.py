# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ����ز�")
@allure.feature("ֱ����ز�")
class Test_Live_Close:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('ֱ����ز�')
    @allure.title("ֱ����ز�")
    def test_live_set_title(self, init_host):
        init_host.start_live()
        init_host.close_liveroom()
        self.base.assert_exist('ֱ������')
        self.base.assert_exist('������ҳ')
