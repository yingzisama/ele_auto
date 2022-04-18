# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ��������������")
@allure.feature("ֱ��������������")
class Test_Live_Tools_Beauty_Skin:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('ֱ��������������')
    @allure.title("����-Ƥ��")
    def test_share_wx(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_tools_beauty_face()
        #ĥƤ
        init_host.live_assert_swipe_value()
        #����
        init_host.live_click_whitening()
        init_host.live_assert_swipe_value()
        #����
        init_host.live_click_ruddy()
        init_host.live_assert_swipe_value()
