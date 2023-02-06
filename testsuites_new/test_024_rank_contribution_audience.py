# coding:gbk
# 自动化测试用例: 贡献榜
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("贡献榜-观众端")
@allure.feature("贡献榜-观众端")
class Test_Rank_Contribution_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('贡献榜-观众端')
    @allure.title("贡献榜-观众端")
    def test_rank_contribution_audience(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击进入榜单
        init_audience.click_rank_audience()
        #获取直播间主播榜单值
        pass
        #退出榜单
        pass
        #赠送礼物
        pass
        #断言榜单值变化
        pass