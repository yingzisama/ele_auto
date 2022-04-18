# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("粉丝团")
@allure.feature("直播间粉丝团")
class Test_Live_Fans_Group:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    @allure.story('主播点击粉丝团')
    @allure.title("查看粉丝团")
    def test_click_fans_group(self, init_host):
        init_host.start_live()
        init_host.click_fans_group()
        self.base.assert_exist('魅力主播榜')

    @allure.story('主播查看粉丝榜')
    @allure.title("查看粉丝榜")
    def test_my_fans_ranktop(self, init_host):
        init_host.start_live()
        init_host.my_fans_ranktop()
        self.base.assert_exist('粉丝榜')

    @allure.story('主播查看主播榜')
    @allure.title("查看主播榜")
    def test_my_streamer_ranking(self, init_host):
        init_host.start_live()
        init_host.my_streamer_ranking()
        self.base.assert_exist('魅力榜')
