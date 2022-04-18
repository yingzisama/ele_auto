# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("��Ϣ��Ƭ-��ע����")
@allure.feature("��Ϣ��Ƭ-��ע����")
class Test_Audience_Host_Shield:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('��ע����')
    @allure.title("��ע����")
    def test_audience_host_shield(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #�����Ϣ��Ƭ-��������
        init_audience.click_hostcard_shield()
        #�����������-����������
        self.base.back()
        self.base.wait_time(1)
        init_audience.click_ele_av_room_top_close()
        self.base.back()
        self.base.wait_time(1)
        self.base.back()
        init_audience.click_mind_shield_manager()
        #���������Ѽ��������
        init_audience.assert_shield_host_exist()
        #��ԭ-�������߳�������
        init_audience.click_shield_host_remove()
