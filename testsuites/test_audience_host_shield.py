# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("信息卡片-关注主播")
@allure.feature("信息卡片-关注主播")
class Test_Audience_Host_Shield:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('关注主播')
    @allure.title("关注主播")
    def test_audience_host_shield(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #点击信息卡片-拉黑主播
        init_audience.click_hostcard_shield()
        #进入个人中心-黑名单管理
        self.base.back()
        self.base.wait_time(1)
        init_audience.click_ele_av_room_top_close()
        self.base.back()
        self.base.wait_time(1)
        self.base.back()
        init_audience.click_mind_shield_manager()
        #断言主播已加入黑名单
        init_audience.assert_shield_host_exist()
        #还原-将主播踢出黑名单
        init_audience.click_shield_host_remove()
