# coding:gbk
# �Զ�����������: ������������ͳɳ�������������ɳ�����
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("����-�����ɳ�����")
@allure.feature("����-�����ɳ�����")
class Test_Gift_Sent_Grow_Unlock:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('�����ɳ�����')
    @allure.title("�����ɳ�����")
    def test_audience_sentgift_grow_unlock(self, init_audience):
        # ��ԭ����
        ele_function.grow_clear()
        # ����ֱ����
        init_audience.enter_live_room()
        # ��ֵ212С���
        ele_function.add_coin(313)
        # ��������
        init_audience.live_click_gift_button()
        # ���ͳɳ�����-õ��100��
        init_audience.live_click_100_grow_gift()
        # ���Գɳ�����-õ�廨��icon(������)����
        init_audience.assert_big_meigui()
        # ����õ�廨��
        init_audience.live_click_grow_gift_bigmeigui()
        # �������Ϊ14
        init_audience.assert_gift_balance(14)
        # �ر����������
        self.base.back()
        self.base.back()
        # ��������������������Ϣ
        init_audience.assert_gift_message()
