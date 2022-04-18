# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("��������-��Ϣ���")
@allure.feature("��������-��Ϣ���")
class Test_Mind_Personal_Check:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ����Ϣ���")
        self.base = self.mind.base
        yield self.mind
        logger.info("������Ϣ���")

    @allure.story('������Ϣ���')
    @allure.title("������Ϣ���")
    def test_mind_personal_check(self, init_live):
        #��mindҳ
        init_live.click_mind_button()
        #�����û�ͷ���ǳơ�С��š��ȼ�ѫ�¡����ҡ�ְҵ����ע���ͷ�˿��Ԫ�ش���
        self.base.assert_image_findit('./aseert_pic/mind_person_name.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_ele_userId.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_countries.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_Focus_on.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_fans.jpg')
        #�����ע��
        self.base.click_descriptionContain('��ע','��ע')
        #���Թ�ע�б�����չʾ����
        self.base.assert_element_exist('com.yiwuzhibo:id/tv_bar_title')
        #����
        self.base.back()
        #�����˿
        self.base.click_descriptionContain('��˿','��˿')
        #���Է�˿�б�����չʾ����
        self.base.assert_element_exist('com.yiwuzhibo:id/tv_bar_title')
