# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("��˿��")
@allure.feature("ֱ�����˿��")
class Test_Live_Fans_Group:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('���������˿��')
    @allure.title("�鿴��˿��")
    def test_click_fans_group(self, init_host):
        init_host.start_live()
        init_host.click_fans_group()
        self.base.assert_exist('����������')

    @allure.story('�����鿴��˿��')
    @allure.title("�鿴��˿��")
    def test_my_fans_ranktop(self, init_host):
        init_host.start_live()
        init_host.my_fans_ranktop()
        self.base.assert_exist('��˿��')

    @allure.story('�����鿴������')
    @allure.title("�鿴������")
    def test_my_streamer_ranking(self, init_host):
        init_host.start_live()
        init_host.my_streamer_ranking()
        self.base.assert_exist('������')
