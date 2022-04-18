# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("我的收益")
@allure.feature("我的收益")
class Test_Mind_My_Earnings:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("初始化我的收益模块")
        self.base = self.mind.base
        yield self.mind
        logger.info("结束我的收益模块")

    @allure.story('我的收益')
    @allure.title("我的收益")
    def test_mind_my_earnings(self, init_live):
        #进入我的收益页面
        init_live.click_mind_host_center_my_earnings()
        #断言我的收益页面展示正常
        init_live.assert_mind_my_earnings()
