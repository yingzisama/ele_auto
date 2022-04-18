# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("信息卡片-个人主页")
@allure.feature("信息卡片-个人主页")
class Test_Audience_Person_Detail:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('点击个人主页')
    @allure.title("查看主播主页信息")
    def test_audience_person_detail(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #点击信息卡片-主页
        init_audience.click_hostcard_homepage()
        self.base.wait_time()
        #断言
        init_audience.assert_host_person_detail()
