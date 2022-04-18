# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("׼������-Ƥ������")
@allure.feature("׼������-Ƥ������")
class Test_Live_Beauty_Skin:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.live.base
        yield self.live
        logger.info("����ֱ��׼��ģ��")

    @allure.story('׼������-Ƥ������')
    @allure.title("Ƥ������")
    def test_beauty_skin_cb_color(self, init_live):
        init_live.start_live_prepare()
        init_live.live_beauty_face_tools()
        self.base.assert_exist('����')
        self.base.assert_exist('ĥƤ')
        self.base.assert_exist('����')
        #ĥƤ
        init_live.live_assert_swipe_value()
        #����
        init_live.live_click_whitening()
        init_live.live_assert_swipe_value()
        #����
        init_live.live_click_ruddy()
        init_live.live_assert_swipe_value()
