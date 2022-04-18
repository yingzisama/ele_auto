# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间开播")
@allure.feature("直播间开播")
class Test_Live_premiere:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.live.base
        yield self.live
        logger.info("结束直播准备模块")

    @allure.story('直播间开播')
    @allure.title("直播间开播")
    def test_live_set_title(self, init_live):
        init_live.start_live()
        self.base.assert_exist('贡献榜')
        self.base.assert_exist('粉丝团')
