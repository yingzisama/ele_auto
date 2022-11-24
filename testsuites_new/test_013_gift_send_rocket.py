# coding:gbk
# �Զ�����������: ������������ͺ������
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-�������")
@allure.feature("����-�������")
class Test_Gift_Sent_Rocket:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('���ͺ������')
    @allure.title("���޺������")
    def test_audience_sentgift_rocket(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ15313С���
        ele_function.add_coin(15313)
        # ��������
        init_audience.live_click_gift_button()
        # ���ͺ������-���߹���
        init_audience.live_click_rocket_gift()
        # �������Ϊ313
        init_audience.assert_gift_balance(313)
        # �ر����������
        # self.base.back()
        # # ��������������������Ϣ
        # init_audience.assert_gift_message()