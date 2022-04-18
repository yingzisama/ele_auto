# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("����ֱ���䷢��")
@allure.feature("����ֱ���䷢��")
class Test_Live_Input_Comment:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('����ֱ���䷢��')
    @allure.title("��������")
    def test_my_input_comment(self, init_host):
        init_host.start_live()
        init_host.my_input_comment('��������')
        self.base.wait_time()
        self.base.assert_textContains_exist('��������')
