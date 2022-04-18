# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ����������ú󿪲�")
@allure.feature("ֱ����������ú󿪲�")
class Test_Live_title:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.live.base
        yield self.live
        logger.info("����ֱ��׼��ģ��")

    @allure.story('ֱ����������ú󿪲�')
    @allure.title("���ñ��⿪��")
    def test_live_set_title(self, init_live):
        init_live.start_live_prepare()
        init_live.start_live_set_title('��ӭ�����ҵĵ�ֱ����')
        init_live.start_live_true()
        self.base.assert_exist('���װ�')
