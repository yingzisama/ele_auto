# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("�ҵ��˻�-�����")
@allure.feature("�ҵ��˻�-�����")
class Test_Mind_Account_Elebean_Gift:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ���ҵ��˻�ģ��")
        self.base = self.mind.base
        yield self.mind
        logger.info("�����ҵ��˻�ģ��")

    @allure.story('�ҵ��˻�-�����')
    @allure.title("�ҵ��˻�-�����")
    def test_mind_account_elebean_gift(self, init_live):
        #�����ҵ��˻�ҳ��
        init_live.mind_account_tab()
        #�����˻�-��ҳ
        init_live.mind_accout_elebean()
        self.base.wait_time()
        #��������
        init_live.click_mind_elebean_packet()
        #���������ҳ
        init_live.assert_mind_bean_gift_page()
