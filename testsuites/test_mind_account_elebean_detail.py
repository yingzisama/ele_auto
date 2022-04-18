# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("�ҵ��˻�-����ϸ")
@allure.feature("�ҵ��˻�-����ϸ")
class Test_Mind_Account_Elebean_Detail:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ���ҵ��˻�ģ��")
        self.base = self.mind.base
        yield self.mind
        logger.info("�����ҵ��˻�ģ��")

    @allure.story('�ҵ��˻�-����ϸ')
    @allure.title("�ҵ��˻�-����ϸ")
    def test_mind_account_elebean_detail(self, init_live):
        #�����ҵ��˻�ҳ��
        init_live.mind_account_tab()
        #�����˻�-��ҳ
        init_live.mind_accout_elebean()
        self.base.wait_time()
        #�������ϸ
        init_live.click_mind_elebean_detail()
        #��������ϸҳ
        init_live.assert_mind_bean_detail_page()
