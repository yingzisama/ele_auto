# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("����ֱ������������")
@allure.feature("����ֱ������������")
class Test_Live_Mute_Live:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    @allure.story('����ֱ������������')
    @allure.title("��������")
    def test_live_mute_live(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        self.base.assert_image_findit('./aseert_pic/tpl1638525133804.png')
        init_host.click_liveroom_tools_button_4()
        self.base.assert_image_findit('./aseert_pic/tpl1638524944505.png')
