# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("ֱ�������")
@allure.feature("ֱ�������")
class Test_Live_share:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.live.base
        yield self.live
        logger.info("����ֱ��׼��ģ��")

    #���԰�ǩ����һ�£��޷�����΢�ź�΢������Ȧ
    # @allure.story('ֱ����΢�ŷ���')
    # def test_live_wx(self, init_live):
    #     init_live.start_live_prepare()
    #     init_live.live_share_wx()
    #     self.base.assert_exist()

    # @allure.story('ֱ��������Ȧ����')
    # def test_live_share_wx_circle(self, init_live):
    #     init_live.start_live_prepare()
    #     init_live.live_share_wx_circle()
    #     self.base.assert_exist()

    @allure.story('ֱ����facebook����')
    @allure.title("facebook����")
    def test_live_share_facebook(self, init_live):
        init_live.start_live_prepare()
        init_live.live_share_facebook()
        self.base.assert_exist('facebook')

    @allure.story('ֱ����twitter����')
    def test_live_share_twitter(self, init_live):
        init_live.start_live_prepare()
        init_live.live_share_twitter()
        self.base.assert_textContains_exist('twitter.com')

    @allure.story('ֱ����line����')
    @allure.title("line����")
    def test_live_share_line(self, init_live):
        init_live.start_live_prepare()
        init_live.live_share_line()
        self.base.assert_exist('LINE')
