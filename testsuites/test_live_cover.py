# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ����������ɾ��")
@allure.feature("ֱ����������ɾ��")
class Test_Live_cover:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.live.base
        yield self.live
        logger.info("����ֱ��׼��ģ��")

    @allure.story('ֱ����������ɾ��')
    @allure.title("�������/ɾ��")
    def test_add_cover(self, init_live):
        init_live.start_live_prepare()
        init_live.choose_cover()
        self.base.assert_exist('���')
        init_live.add_first_camera()
        self.base.assert_exist('�����')
        init_live.cover_delete()
        self.base.assert_not_exist('�����')
