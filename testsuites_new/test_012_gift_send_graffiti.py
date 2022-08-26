# coding:gbk
# �Զ�����������: �������������Ϳѻ����
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-Ϳѻ����")
@allure.feature("����-Ϳѻ����")
class Test_Gift_Sent_Graffiti:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('Ϳѻ����')
    @allure.title("Ϳѻ����")
    def test_audience_sentgift_graffiti(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵXXС���
        ele_function.add_coin(111)
        # ��������
        init_audience.live_click_gift_button()
        # ����Ϳѻ����
        init_audience.live_click_graffiti_gift()
        # ��������������������Ϣ
        init_audience.assert_gift_message()
        # ��������
        init_audience.live_click_gift_button()
        # �������Ϊ11
        init_audience.assert_gift_balance(11)
