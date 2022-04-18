# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("准备开播-皮肤设置")
@allure.feature("准备开播-皮肤设置")
class Test_Live_Beauty_Skin:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.live.base
        yield self.live
        logger.info("结束直播准备模块")

    @allure.story('准备开播-皮肤设置')
    @allure.title("皮肤设置")
    def test_beauty_skin_cb_color(self, init_live):
        init_live.start_live_prepare()
        init_live.live_beauty_face_tools()
        self.base.assert_exist('美白')
        self.base.assert_exist('磨皮')
        self.base.assert_exist('红润')
        #磨皮
        init_live.live_assert_swipe_value()
        #美白
        init_live.live_click_whitening()
        init_live.live_assert_swipe_value()
        #红润
        init_live.live_click_ruddy()
        init_live.live_assert_swipe_value()
