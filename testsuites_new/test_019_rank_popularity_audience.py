# coding:gbk
# 自动化测试用例: 人气榜
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("人气榜-观众端")
@allure.feature("人气榜-观众端")
class Test_Rank_Popularity_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('人气榜-日榜-观众端')
    @allure.title("人气榜-日榜-观众端")
    def test_rank_popularity_audience(self, init_audience):
        #进入直播间
        init_audience.enter_live_room()
        #点击人气榜单
        init_audience.click_rank_host()
        #获取直播间主播榜单值
        hot_rank_value1 = self.base.get_popularity_rank_xpath('//*[@resource-id="com.yiwuzhibo:id/fly_user_info"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]')
        #退出榜单
        self.base.back()
        #赠送礼物
        init_audience.live_click_gift_button()
        init_audience.live_click_10coin_gift()
        self.base.back()
        # 打开榜单
        init_audience.click_rank_host()
        # 断言榜单值变化
        hot_rank_value2 = self.base.get_popularity_rank_xpath('//*[@resource-id="com.yiwuzhibo:id/fly_user_info"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]')
        self.base.assert_change_value(hot_rank_value1,hot_rank_value2,10)
        