# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("�ҵ��˻�-С��ҳ�ֵ")
@allure.feature("�ҵ��˻�-С��ҳ�ֵ")
class Test_Mind_Account:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ���ҵ��˻�ģ��")
        self.base = self.mind.base
        yield self.mind
        logger.info("�����ҵ��˻�ģ��")

    @allure.story('�ҵ��˻�-С��ҳ�ֵ')
    @allure.title("�ҵ��˻�-С��ҳ�ֵ")
    def test_mind_account(self, init_live):
        #�����ҵ��˻�ҳ��
        init_live.mind_account_tab()
        #�������Ԫ�ش���
        init_live.assert_mind_account_element_exits()
        #����С��ҳ�ֵҳ
        init_live.click_ele_conin_bk()
        #���Գ�ֵҳ��Ԫ�ش���
        init_live.assert_ele_conin_page()
        #ѡ���һ����ֵ��λ�������ֵҳ
        init_live.click_mind_account_gear_01()
        #���Գ�ֵҳԪ������
        init_live.assert_account_gear_page()
