# coding:gbk
# �Զ�����������: �������������С�����������combo
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-С�����������combo")
@allure.feature("����-С�����������combo")
class Test_Gift_Sent_Coin_Combo:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('����С�����������combo')
    @allure.title("����С�����������combo")
    def test_audience_sentgift_coin_combo(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ99С���
        ele_function.add_coin(79)
        # ��������
        init_audience.live_click_gift_button()
        # ����С��ң�10С��ң����͵�����
        init_audience.live_click_10coin_gift_combo()
        # �������Ϊ90
        init_audience.assert_gift_balance(59)
        # �ر����������
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()