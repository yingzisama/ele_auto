# coding:gbk
# �Զ�����������: ���ǰ�
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("���ǰ�-���ڶ�")
@allure.feature("���ǰ�-���ڶ�")
class Test_Rank_WeekStar_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('���ǰ�-���ڶ�')
    @allure.title("���ǰ�-���ڶ�")
    def test_rank_weekstar_audience(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #��������
        init_audience.click_rank_host()
        init_audience.click_weekstar_rank_tab()
        #��ȡֱ����������ֵ
        pass
        #�˳���
        pass
        #��������
        pass
        #���԰�ֵ�仯
        pass