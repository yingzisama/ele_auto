# coding:gbk
# �Զ�����������: ����ֱ���䣬������һ��
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
import time

logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ����-��һ��")
@allure.feature("ֱ����-��һ������")
class Test_Chuo_Yi_Chuo:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('�ȴ���һ��')
    @allure.title("�ȴ���һ��")
    def test_wait_chuoyichuo(self, init_audience):
        # ����ֱ����
        init_audience.enter_live_room()
        # �ȴ�15s
        time.sleep(15)