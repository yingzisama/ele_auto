# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("��Ϣ��Ƭ-�ٱ�����")
@allure.feature("��Ϣ��Ƭ-�ٱ�����")
class Test_Audience_Host_Report:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('�ٱ�����')
    @allure.title("�ٱ�����")
    def test_audience_host_report(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #����ٱ�
        init_audience.click_ele_hostcard_report()
        self.base.wait_time()
        #����ٱ�����
        self.base.click_description('ɫ�����','ɫ�����')
        #����ٱ�����
        init_audience.input_report_content('������ɫ��')
        #�ύ
        init_audience.click_report_submit()
        #���Ծٱ��ɹ�toast
        init_audience.assert_report_success()
