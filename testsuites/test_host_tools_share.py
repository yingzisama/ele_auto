# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.host import Host
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ��������������")
@allure.feature("ֱ��������������")
class Test_Live_Tools_Share:
    @pytest.fixture
    def init_host(self):
        self.host = Host(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.host.base
        yield self.host
        logger.info("����ֱ��׼��ģ��")

    # @allure.story('ֱ��������������')
    # @allure.title("΢�ŷ���")
    # def test_share_wx(self, init_host):
    #     init_host.start_live()
    #     init_host.click_liveroom_fun_more()
    #     init_host.swipe_downtools_left()
    #     self.base.assert_exist('����')
    #     init_host.click_liveroom_tools_button_1()
    #     init_host.click_liveroom_share_wx()

    # @allure.story('ֱ��������������')
    # @allure.title("����Ȧ����")
    # def test_share_Circlefriends(self, init_host):
    #     init_host.start_live()
    #     init_host.click_liveroom_fun_more()
    #     init_host.swipe_downtools_left()
    #     self.base.assert_exist('����')
    #     init_host.click_liveroom_tools_button_1()
    #     init_host.click_liveroom_share_Circlefriends()

    @allure.story('ֱ��������������')
    @allure.title("Facebook����")
    def test_share_Circlefriends(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        init_host.swipe_downtools_left()
        self.base.assert_exist('����')
        init_host.click_liveroom_tools_button_1()
        init_host.click_liveroom_share_Facebook()
        self.base.assert_exist('facebook')

    @allure.story('ֱ��������������')
    @allure.title("Twitter����")
    def test_share_Twitter(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        init_host.swipe_downtools_left()
        self.base.assert_exist('����')
        init_host.click_liveroom_tools_button_1()
        init_host.click_liveroom_share_Twitter()
        self.base.assert_textContains_exist('twitter.com')

    @allure.story('ֱ��������������')
    @allure.title("Line����")
    def test_share_Line(self, init_host):
        init_host.start_live()
        init_host.click_liveroom_fun_more()
        init_host.swipe_downtools_left()
        self.base.assert_exist('����')
        init_host.click_liveroom_tools_button_1()
        init_host.swipe_downtools_left()
        self.base.assert_exist('Line')
        init_host.click_liveroom_share_Line()
        self.base.assert_exist('LINE')
