# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("�ҵ�����")
@allure.feature("�ҵ�����")
class Test_Mind_My_Earnings:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ���ҵ�����ģ��")
        self.base = self.mind.base
        yield self.mind
        logger.info("�����ҵ�����ģ��")

    @allure.story('�ҵ�����')
    @allure.title("�ҵ�����")
    def test_mind_my_earnings(self, init_live):
        #�����ҵ�����ҳ��
        init_live.click_mind_host_center_my_earnings()
        #�����ҵ�����ҳ��չʾ����
        init_live.assert_mind_my_earnings()
