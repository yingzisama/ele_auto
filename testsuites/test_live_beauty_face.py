# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("准备开播-美颜设置")
@allure.feature("准备开播-美颜设置")
class Test_Live_Beauty_Face:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.live.base
        yield self.live
        logger.info("结束直播准备模块")

    @allure.story('准备开播-美颜设置')
    @allure.title("美颜设置")
    def test_beauty_face_cb_color(self, init_live):
        init_live.start_live_prepare()
        init_live.live_beauty_face_tools()
        #face
        init_live.live_click_cb_shape()
        self.base.assert_exist('大眼')
        self.base.assert_exist('瘦脸')
        self.base.assert_exist('下巴')
        self.base.assert_exist('额头')
        self.base.assert_exist('瘦鼻')
        self.base.assert_exist('嘴型')
        #大眼
        init_live.live_click_big_eye()
        init_live.live_assert_swipe_value()
        #瘦脸
        init_live.live_click_thin_face()
        init_live.live_assert_swipe_value()
        #下巴
        init_live.live_click_chin_face()
        init_live.live_assert_swipe_value()
        #额头
        init_live.live_click_forehead_face()
        init_live.live_assert_swipe_value() 
        #瘦鼻
        init_live.live_click_nose_face()
        init_live.live_assert_swipe_value() 
        #嘴型
        init_live.live_click_mouth_face()
        init_live.live_assert_swipe_value()
