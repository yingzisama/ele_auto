# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("��Ϣ��Ƭ-@����")
@allure.feature("��Ϣ��Ƭ-@����")
class Test_Audience_Host_Eit:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('���������ҳ')
    @allure.title("@����-���͵�Ļ")
    def test_audience_host_eit(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #�����Ϣ��Ƭ-��ҳ
        init_audience.click_hostcard_eit()
        self.base.wait_time()
        #����111
        self.base.set_text_FastInputIME('111','���뵯Ļ111')
        #�������
        init_audience.click_input_confirm_tv()
        #���Թ������ָ÷���
        init_audience.assert_live_room_im()
