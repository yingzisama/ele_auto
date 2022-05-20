# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("������")
@allure.feature("������")
class Test_Audience_Sendgift_Bean:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('������')
    @allure.title("������")
    def test_audience_sendgift_bean(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #��ȡֱ���䵱ǰ���Ǳ���ˮ

        #�������ť�����������
        
        #��ȡ��ǰ�����

        #ѡ�������ȷ������

        #�鿴ʣ����

        #����������󶹼��٣��������Ǳ�����