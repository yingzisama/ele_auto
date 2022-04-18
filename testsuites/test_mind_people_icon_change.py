# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("��������-��ͷ��")
@allure.feature("��������-��ͷ��")
class Test_Mind_People_Center_Icon:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ��ֱ��׼��ģ��")
        self.base = self.mind.base
        yield self.mind
        logger.info("����ֱ��׼��ģ��")

    @allure.story('����ͷ�����')
    @allure.title("����ͷ�����")
    def test_mind_people_icon_change(self, init_live):
        #����������ҳ
        init_live.click_people_data()
        #������ǰ�û�ͷ��
        init_live.save_element_pic('people_icon')
        #���գ�����ͷ��
        init_live.change_people_icon()
        #��������֮ǰ�ڵ�ǰҳ�治����
        self.base.assert_not_image_findit('./aseert_pic/people_icon.jpg')
