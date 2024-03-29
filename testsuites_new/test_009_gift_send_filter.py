# coding:gbk
# �Զ�����������: ��������������˾�����
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-�˾�����")
@allure.feature("����-�˾�����")
class Test_Gift_Sent_Filter:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('����-�˾�����')
    @allure.title("����-�˾�����")
    def test_audience_sentgift_filter(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ111С���
        ele_function.add_coin(111)
        # ��������
        init_audience.live_click_gift_button()
        # �����˾�����-���ﻨ��
        init_audience.live_click_filter_gift()
        # �������Ϊ11
        init_audience.assert_gift_balance(11)
        # �ر����������
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()