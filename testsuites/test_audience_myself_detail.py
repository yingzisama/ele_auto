# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ������-������Ϣ��Ƭ")
@allure.feature("ֱ������-������Ϣ��Ƭ")
class Test_Audience_Myself_Detail:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('��������Լ�ͷ��')
    @allure.title("�鿴������Ϣ")
    def test_audience_myself_detail(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #�����Ϣ��Ƭ-��ҳ
        init_audience.click_hostcard_homepage()
        self.base.wait_time()
        #����
        init_audience.assert_host_person_detail()
