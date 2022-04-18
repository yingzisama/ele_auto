# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("�ҵ��˻�-С�����ϸ")
@allure.feature("�ҵ��˻�-С�����ϸ")
class Test_Mind_Account_Eleconin_Detail:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ���ҵ��˻�ģ��")
        self.base = self.mind.base
        yield self.mind
        logger.info("�����ҵ��˻�ģ��")

    @allure.story('�ҵ��˻�-С�����ϸ')
    @allure.title("�ҵ��˻�-С�����ϸ")
    def test_mind_account_eleconin_detail(self, init_live):
        #�����ҵ��˻�ҳ��
        init_live.mind_account_tab()
        #����С��ң������ϸҳ
        init_live.mind_accout_elecoin()
        init_live.click_mind_account_tv_bar_right()
        #���������ϸ������tab��֧��tab����
        init_live.assert_account_eleconin_detail()
