# coding:gbk
# �Զ�����������: ������������ͳɳ���������
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-�ɳ���������")
@allure.feature("����-�ɳ���������")
class Test_Gift_Sent_Grow:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('���ͳɳ���������')
    @allure.title("���ͳɳ���������")
    def test_audience_sentgift_grow(self, init_audience):
        # ��ԭ����
        ele_function.grow_clear()
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ99С���
        ele_function.add_coin(37)
        # ��������
        init_audience.live_click_gift_button()
        # ���ͳɳ�����-õ��
        init_audience.live_click_2coin_grow_gift()
        # �������Ϊ90
        init_audience.assert_gift_balance(35)
        # �ر����������
        self.base.back()
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()