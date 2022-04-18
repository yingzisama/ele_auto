# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间内美颜设置")
@allure.feature("直播间内美颜设置")
class Test_Live_Tools_Beauty_Skin:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    @allure.story('直播间内美颜设置')
    @allure.title("美颜-皮肤")
    def test_share_wx(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_tools_beauty_face()
        #磨皮
        init_host.live_assert_swipe_value()
        #美白
        init_host.live_click_whitening()
        init_host.live_assert_swipe_value()
        #红润
        init_host.live_click_ruddy()
        init_host.live_assert_swipe_value()
