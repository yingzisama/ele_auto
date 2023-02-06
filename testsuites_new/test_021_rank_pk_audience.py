# coding:gbk
# �Զ�����������: PK��
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("pk��-���ڶ�")
@allure.feature("pk��-���ڶ�")
class Test_Rank_Pk_Audience:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('pk��-���ڶ�')
    @allure.title("pk��-���ڶ�")
    def test_rank_pk_audience(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #��������
        init_audience.click_rank_host()
        init_audience.click_pk_rank_tab()
        #��ȡֱ����������ֵ
        pass
        #�˳���
        pass
        #��������
        pass
        #���԰�ֵ�仯
        pass
        