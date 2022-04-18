# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("主播头像-信息卡片")
@allure.feature("主播头像-信息卡片")
class Test_Audience_Enter_Live_Room:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('点击主播头像')
    @allure.title("查看主播信息卡片")
    def test_audience_enter_live_room(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #断言直播间界面各元素存在
        init_audience.assert_live_room_element()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #断言信息卡片元素展示正常
        init_audience.assert_host_layout_bg()
