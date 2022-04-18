# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间内美颜设置")
@allure.feature("直播间内美颜设置")
class Test_Live_Tools_Beauty_Face:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    @allure.story('直播间内美颜设置')
    @allure.title("美颜-脸型")
    def test_share_wx(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_tools_beauty_face()
        #face
        init_host.live_click_cb_shape()
        self.base.assert_exist('大眼')
        self.base.assert_exist('瘦脸')
        self.base.assert_exist('下巴')
        self.base.assert_exist('额头')
        self.base.assert_exist('瘦鼻')
        self.base.assert_exist('嘴型')
        #大眼
        init_host.live_click_big_eye()
        init_host.live_assert_swipe_value()
        #瘦脸
        init_host.live_click_thin_face()
        init_host.live_assert_swipe_value()
        #下巴
        init_host.live_click_chin_face()
        init_host.live_assert_swipe_value()
        #额头
        init_host.live_click_forehead_face()
        init_host.live_assert_swipe_value() 
        #瘦鼻
        init_host.live_click_nose_face()
        init_host.live_assert_swipe_value() 
        #嘴型
        init_host.live_click_mouth_face()
        init_host.live_assert_swipe_value()
