# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间标题设置后开播")
@allure.feature("直播间标题设置后开播")
class Test_Live_title:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.live.base
        yield self.live
        logger.info("结束直播准备模块")

    @allure.story('直播间标题设置后开播')
    @allure.title("设置标题开播")
    def test_live_set_title(self, init_live):
        init_live.start_live_prepare()
        init_live.start_live_set_title('欢迎来到我的的直播间')
        init_live.start_live_true()
        self.base.assert_exist('贡献榜')
