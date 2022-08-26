# coding:gbk
# �Զ�����������: �������������С�����������
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-С�����������")
@allure.feature("����-С�����������")
class Test_Gift_Sent_Coin:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('����С�����������')
    @allure.title("����С�����������")
    def test_audience_sentgift_coin(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ99С���
        ele_function.add_coin(99)
        # ��������
        init_audience.live_click_gift_button()
        # ����С��ң�10С��ң����͵�����
        init_audience.live_click_10coin_gift()
        # �������Ϊ89
        init_audience.assert_gift_balance(89)
        # �ر����������
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()