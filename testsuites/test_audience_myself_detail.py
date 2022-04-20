# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间内-观众信息卡片")
@allure.feature("直播间内-观众信息卡片")
class Test_Audience_Myself_Detail:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('点击观众自己头像')
    @allure.title("查看观众信息")
    def test_audience_myself_detail(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #点击信息卡片-主页
        init_audience.click_hostcard_homepage()
        self.base.wait_time()
        #断言
        init_audience.assert_host_person_detail()
