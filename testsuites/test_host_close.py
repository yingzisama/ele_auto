# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间关播")
@allure.feature("直播间关播")
class Test_Live_Close:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    @allure.story('直播间关播')
    @allure.title("直播间关播")
    def test_live_set_title(self, init_host):
        init_host.start_live()
        init_host.close_liveroom()
        self.base.assert_exist('直播结束')
        self.base.assert_exist('返回首页')
