# coding:gbk
# �Զ�����������: ������
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("������-���ڶ�")
@allure.feature("������-���ڶ�")
class Test_Rank_Popularity_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('������-�հ�-���ڶ�')
    @allure.title("������-�հ�-���ڶ�")
    def test_rank_popularity_audience(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #���������
        init_audience.click_rank_host()
        #��ȡֱ����������ֵ
        hot_rank_value1 = self.base.get_popularity_rank_xpath('//*[@resource-id="com.yiwuzhibo:id/fly_user_info"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]')
        #�˳���
        self.base.back()
        #��������
        init_audience.live_click_gift_button()
        init_audience.live_click_10coin_gift()
        self.base.back()
        # �򿪰�
        init_audience.click_rank_host()
        # ���԰�ֵ�仯
        hot_rank_value2 = self.base.get_popularity_rank_xpath('//*[@resource-id="com.yiwuzhibo:id/fly_user_info"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]')
        self.base.assert_change_value(hot_rank_value1,hot_rank_value2,10)
        