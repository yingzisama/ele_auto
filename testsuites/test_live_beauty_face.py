# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("׼������-��������")
@allure.feature("׼������-��������")
class Test_Live_Beauty_Face:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.live.base
        yield self.live
        logger.info("����ֱ��׼��ģ��")

    @allure.story('׼������-��������')
    @allure.title("��������")
    def test_beauty_face_cb_color(self, init_live):
        init_live.start_live_prepare()
        init_live.live_beauty_face_tools()
        #face
        init_live.live_click_cb_shape()
        self.base.assert_exist('����')
        self.base.assert_exist('����')
        self.base.assert_exist('�°�')
        self.base.assert_exist('��ͷ')
        self.base.assert_exist('�ݱ�')
        self.base.assert_exist('����')
        #����
        init_live.live_click_big_eye()
        init_live.live_assert_swipe_value()
        #����
        init_live.live_click_thin_face()
        init_live.live_assert_swipe_value()
        #�°�
        init_live.live_click_chin_face()
        init_live.live_assert_swipe_value()
        #��ͷ
        init_live.live_click_forehead_face()
        init_live.live_assert_swipe_value() 
        #�ݱ�
        init_live.live_click_nose_face()
        init_live.live_assert_swipe_value() 
        #����
        init_live.live_click_mouth_face()
        init_live.live_assert_swipe_value()
