# coding:gbk
# �Զ�����������: ���װ�
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("���װ�-���ڶ�")
@allure.feature("���װ�-���ڶ�")
class Test_Rank_Contribution_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('���װ�-���ڶ�')
    @allure.title("���װ�-���ڶ�")
    def test_rank_contribution_audience(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #��������
        init_audience.click_rank_audience()
        #��ȡֱ����������ֵ
        pass
        #�˳���
        pass
        #��������
        pass
        #���԰�ֵ�仯
        pass