# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("主播直播间发言")
@allure.feature("主播直播间发言")
class Test_Live_Input_Comment:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    @allure.story('主播直播间发言')
    @allure.title("主播发言")
    def test_my_input_comment(self, init_host):
        init_host.start_live()
        init_host.my_input_comment('主播发言')
        self.base.wait_time()
        self.base.assert_textContains_exist('主播发言')
