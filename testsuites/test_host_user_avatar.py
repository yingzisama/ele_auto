# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("主播直播间点击头像")
@allure.feature("主播直播间点击头像")
class Test_Live_User_avatar:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    @allure.story('主播点击自己头像')
    @allure.title("弹出信息卡片")
    def test_live_set_title(self, init_host):
        init_host.start_live()
        init_host.click_user_avatar()
        self.base.assert_exist('粉丝')
        self.base.assert_exist('关注')
        self.base.assert_exist('送出')
        self.base.assert_exist('收到')
