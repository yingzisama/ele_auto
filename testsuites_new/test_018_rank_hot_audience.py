# coding:gbk
# �Զ�����������: �ȶȰ�����
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("�ȶȰ�-���ڶ�")
@allure.feature("�ȶȰ�-���ڶ�")
class Test_Rank_Hot_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('�ȶȰ�-���ڶ�')
    @allure.title("�ȶȰ�-���ڶ�")
    def test_rank_hot_audience(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #����ȶȰ�
        init_audience.click_rank_host()
        init_audience.click_hot_rank_tab()
        #��ȡֱ����������ֵ
        hot_rank_value1 = self.base.get_hot_rank_xpath('//*[@resource-id="com.yiwuzhibo:id/fly_user_info"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]')
        #�˳���
        self.base.back()
        #����1K����
        init_audience.live_click_gift_button()
        init_audience.live_click_1000coin_gift()
        self.base.back()
        # �򿪰�
        init_audience.click_rank_host()
        init_audience.click_hot_rank_tab()
        #��ȡֱ����������ֵ
        hot_rank_value2 = self.base.get_hot_rank_xpath('//*[@resource-id="com.yiwuzhibo:id/fly_user_info"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]')
        # ���԰�ֵ�仯
        init_audience.assert_change_value(hot_rank_value1,hot_rank_value2,1)