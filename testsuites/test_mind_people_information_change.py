# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("��������-���ø�����Ϣ")
@allure.feature("��������-���ø�����Ϣ")
class Test_Mind_People_Information_Change:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("��ʼ���޸ĸ�����Ϣ����")
        self.base = self.mind.base
        yield self.mind
        logger.info("�޸ĸ�����Ϣ����")

    @allure.story('��������-��Ϣ�޸�')
    @allure.title("��������-��Ϣ�޸�")
    def test_mind_people_information_change(self, init_live):
        #����������ҳ
        init_live.click_people_data()
        #�޸��ǳƣ������Զ������ԡ�������������
        init_live.change_mind_nickname('��������')
        #�޸��Ա𣨲����������У�
        init_live.change_mind_sex('��')
        #�޸Ĺ���/����������������������
        init_live.change_mind_countries_aman()
        #�޸ĳ��У����������Ϻ���
        init_live.change_mind_city('�Ϻ�')
        #�޸�����
        init_live.change_mind_birthday()
        #�޸�ְҵ����ְҵ����������
        init_live.change_mind_professional('����')
        #�ϻ����鿴����
        self.base.back()
        self.base.wait_time()
        self.base.swipe_up()
        #�޸ĸ���ǩ����û�и���ǩ������û�и���ǩ��2��
        init_live.change_mind_signature('û�и���ǩ��2')
        #�˻ص�mindҳ
        init_live.editor_information_done()
        self.base.back()
        #�����޸���Ч���ǳ��޸ĳɹ��������Ա�icon�����ֹ��ң���������������ְҵ��
        init_live.assert_host_information_change_success()
        #��ԭ�޸�
        init_live.reduction_mind_information('�����Զ�������')
        #����޸�
        init_live.editor_information_done()
