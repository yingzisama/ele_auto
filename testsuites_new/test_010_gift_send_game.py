# coding:gbk
# �Զ�����������: ���������������Ϸ����
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-��Ϸ����")
@allure.feature("����-��Ϸ����")
class Test_Gift_Sent_Game:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('������Ϸ����')
    @allure.title("������Ϸ����")
    def test_audience_sentgift_game(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ12С���
        ele_function.add_coin(12)
        # ��������
        init_audience.live_click_gift_button()
        # ��������-����������
        init_audience.live_click_game_gift()
        # �������Ϊ11
        init_audience.assert_gift_balance(11)
        # �ر����������
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()