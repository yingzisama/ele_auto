# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("��Ϣ��Ƭ-��ע����")
@allure.feature("��Ϣ��Ƭ-��ע����")
class Test_Audience_Host_Focus:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('��ע����')
    @allure.title("��ע����")
    def test_audience_host_focus(self, init_audience):
        #����ֱ����
        init_audience.enter_live_room()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #��ȡ��ǰ��˿��
        fans_1 = init_audience.get_hostcard_fans_num()
        #�����Ϣ��Ƭ-ȡ����ע
        init_audience.click_hostcard_focus()
        self.base.wait_time(10)
        self.base.back()
        #�������ͷ�񣬵�����Ϣ��Ƭ
        init_audience.click_ele_user_avatar()
        #��ȡ��ǰ��˿��
        fans_2 = init_audience.get_hostcard_fans_num()
        #��ԭ��ע״̬
        init_audience.click_hostcard_focus()
        #���Է�˿��-1
        assert fans_2 == fans_1 - 1
