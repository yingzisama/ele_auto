# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("С�������")
@allure.feature("С�������")
class Test_Audience_Sendgift_Coin:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('С�������')
    @allure.title("С�������")
    def test_audience_sendgift_coin(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #��ȡֱ���䵱ǰ���Ǳ���ˮ

        #�������ť�����������
        
        #��ȡ��ǰС������

        #ѡ��С������ȷ������

        #�鿴ʣ��С���

        #���������С��Ҽ��٣��������Ǳ�����