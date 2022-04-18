# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("信息卡片-关注主播")
@allure.feature("信息卡片-关注主播")
class Test_Audience_Host_Focus:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('关注主播')
    @allure.title("关注主播")
    def test_audience_host_focus(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #获取当前粉丝数
        fans_1 = init_audience.get_hostcard_fans_num()
        #点击信息卡片-取消关注
        init_audience.click_hostcard_focus()
        self.base.wait_time(10)
        self.base.back()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #获取当前粉丝数
        fans_2 = init_audience.get_hostcard_fans_num()
        #还原关注状态
        init_audience.click_hostcard_focus()
        #断言粉丝数-1
        assert fans_2 == fans_1 - 1
