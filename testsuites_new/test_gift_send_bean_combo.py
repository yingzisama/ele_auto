# coding:gbk
# �Զ�����������: �����������������������combo
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-����������combo")
@allure.feature("����-����������combo")
class Test_Gift_Sent_Bean:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('��������������combo')
    @allure.title("��������������combo")
    def test_audience_sentgift_coin(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ67��
        ele_function.add_bean(67)
        # ��������
        init_audience.live_click_gift_button()
        # ����20������combo
        init_audience.live_click_20bean_gift_combo()
        # �������Ϊ77
        init_audience.assert_gift_balance(27)
        # �ر����������
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()