# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间内主播分享")
@allure.feature("直播间内主播分享")
class Test_Live_Tools_Share:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.host.base
        yield self.host
        logger.info("结束直播准备模块")

    # @allure.story('直播间内主播分享')
    # @allure.title("微信分享")
    # def test_share_wx(self, init_host):
    #     init_host.start_live()
    #     init_host.click_liveroom_fun_more()
    #     init_host.swipe_downtools_left()
    #     self.base.assert_exist('分享')
    #     init_host.click_liveroom_tools_button_1()
    #     init_host.click_liveroom_share_wx()

    # @allure.story('直播间内主播分享')
    # @allure.title("朋友圈分享")
    # def test_share_Circlefriends(self, init_host):
    #     init_host.start_live()
    #     init_host.click_liveroom_fun_more()
    #     init_host.swipe_downtools_left()
    #     self.base.assert_exist('分享')
    #     init_host.click_liveroom_tools_button_1()
    #     init_host.click_liveroom_share_Circlefriends()

    @allure.story('直播间内主播分享')
    @allure.title("Facebook分享")
    def test_share_Circlefriends(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        init_host.swipe_downtools_left()
        self.base.assert_exist('分享')
        init_host.click_liveroom_tools_button_1()
        init_host.click_liveroom_share_Facebook()
        self.base.assert_exist('facebook')

    @allure.story('直播间内主播分享')
    @allure.title("Twitter分享")
    def test_share_Twitter(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        init_host.swipe_downtools_left()
        self.base.assert_exist('分享')
        init_host.click_liveroom_tools_button_1()
        init_host.click_liveroom_share_Twitter()
        self.base.assert_textContains_exist('twitter.com')

    @allure.story('直播间内主播分享')
    @allure.title("Line分享")
    def test_share_Line(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        init_host.swipe_downtools_left()
        self.base.assert_exist('分享')
        init_host.click_liveroom_tools_button_1()
        init_host.swipe_downtools_left()
        self.base.assert_exist('Line')
        init_host.click_liveroom_share_Line()
        self.base.assert_exist('LINE')
