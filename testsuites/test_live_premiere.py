# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ���俪��")
@allure.feature("ֱ���俪��")
class Test_Live_premiere:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.live.base
        yield self.live
        logger.info("����ֱ��׼��ģ��")

    @allure.story('ֱ���俪��')
    @allure.title("ֱ���俪��")
    def test_live_set_title(self, init_live):
        init_live.start_live()
        self.base.assert_exist('���װ�')
        self.base.assert_exist('��˿��')
