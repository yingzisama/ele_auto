# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("����ֱ������ͷ��")
@allure.feature("����ֱ������ͷ��")
class Test_Live_User_avatar:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('��������Լ�ͷ��')
    @allure.title("������Ϣ��Ƭ")
    def test_live_set_title(self, init_host):
        init_host.start_live()
        init_host.click_user_avatar()
        self.base.assert_exist('��˿')
        self.base.assert_exist('��ע')
        self.base.assert_exist('�ͳ�')
        self.base.assert_exist('�յ�')
