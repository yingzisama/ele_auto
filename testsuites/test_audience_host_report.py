# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("信息卡片-举报主播")
@allure.feature("信息卡片-举报主播")
class Test_Audience_Host_Report:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('举报主播')
    @allure.title("举报主播")
    def test_audience_host_report(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击主播头像，弹出信息卡片
        init_audience.click_ele_user_avatar()
        #点击举报
        init_audience.click_ele_hostcard_report()
        self.base.wait_time()
        #点击举报类型
        self.base.click_description('色情低俗','色情低俗')
        #输入举报内容
        init_audience.input_report_content('主播很色情')
        #提交
        init_audience.click_report_submit()
        #断言举报成功toast
        init_audience.assert_report_success()
