# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("小象币送礼")
@allure.feature("小象币送礼")
class Test_Audience_Sendgift_Coin:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('小象币送礼')
    @allure.title("小象币送礼")
    def test_audience_sendgift_coin(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #获取直播间当前星星币流水

        #点击送礼按钮，打开礼物面板
        
        #获取当前小象币余额

        #选择小象币礼物，确定送礼

        #查看剩余小象币

        #断言送礼后，小象币减少，主播星星币增加