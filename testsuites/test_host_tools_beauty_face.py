# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ��������������")
@allure.feature("ֱ��������������")
class Test_Live_Tools_Beauty_Face:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('ֱ��������������')
    @allure.title("����-����")
    def test_share_wx(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_tools_beauty_face()
        #face
        init_host.live_click_cb_shape()
        self.base.assert_exist('����')
        self.base.assert_exist('����')
        self.base.assert_exist('�°�')
        self.base.assert_exist('��ͷ')
        self.base.assert_exist('�ݱ�')
        self.base.assert_exist('����')
        #����
        init_host.live_click_big_eye()
        init_host.live_assert_swipe_value()
        #����
        init_host.live_click_thin_face()
        init_host.live_assert_swipe_value()
        #�°�
        init_host.live_click_chin_face()
        init_host.live_assert_swipe_value()
        #��ͷ
        init_host.live_click_forehead_face()
        init_host.live_assert_swipe_value() 
        #�ݱ�
        init_host.live_click_nose_face()
        init_host.live_assert_swipe_value() 
        #����
        init_host.live_click_mouth_face()
        init_host.live_assert_swipe_value()
