# coding:gbk
# �Զ�����������: ��ҳ���banner�ɹ���ת
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("���-banner")
@allure.feature("���-banner")
class Test_Banner_Click:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("��ʼ������ֱ����")
        self.base = self.audience.base
        yield self.audience
        logger.info("��������ֱ����")

    @allure.story('�����ҳbanner')
    @allure.title("�����ҳbanner")
    def test_click_banner(self, init_audience):
        # ����ӡ������Ƽ�ҳ(�������-Խ��)
        init_audience.live_click_VNpage()
        # ���banner����ת��ָ��ֱ����
        init_audience.live_click_banner()
        # ����ֱ����Ԫ�ش���
        init_audience.assert_live_room()
        