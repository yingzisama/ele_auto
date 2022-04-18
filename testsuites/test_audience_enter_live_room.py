# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("����ͷ��-��Ϣ��Ƭ")
@allure.feature("����ͷ��-��Ϣ��Ƭ")
class Test_Audience_Enter_Live_Room:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('�������ͷ��')
    @allure.title("�鿴������Ϣ��Ƭ")
    def test_audience_enter_live_room(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #����ֱ��������Ԫ�ش���
        init_audience.assert_live_room_element()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #������Ϣ��ƬԪ��չʾ����
        init_audience.assert_host_layout_bg()
