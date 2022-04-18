# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间分享")
@allure.feature("直播间分享")
class Test_Live_share:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.live.base
        yield self.live
        logger.info("结束直播准备模块")

    #测试包签名不一致，无法分享到微信和微信朋友圈
    # @allure.story('直播间微信分享')
    # def test_live_wx(self, init_live):
    #     init_live.start_live_prepare()
    #     init_live.live_share_wx()
    #     self.base.assert_exist()

    # @allure.story('直播间朋友圈分享')
    # def test_live_share_wx_circle(self, init_live):
    #     init_live.start_live_prepare()
    #     init_live.live_share_wx_circle()
    #     self.base.assert_exist()

    @allure.story('直播间facebook分享')
    @allure.title("facebook分享")
    def test_live_share_facebook(self, init_live):
        init_live.start_live_prepare()
        init_live.live_share_facebook()
        self.base.assert_exist('facebook')

    @allure.story('直播间twitter分享')
    def test_live_share_twitter(self, init_live):
        init_live.start_live_prepare()
        init_live.live_share_twitter()
        self.base.assert_textContains_exist('twitter.com')

    @allure.story('直播间line分享')
    @allure.title("line分享")
    def test_live_share_line(self, init_live):
        init_live.start_live_prepare()
        init_live.live_share_line()
        self.base.assert_exist('LINE')
