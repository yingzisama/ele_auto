# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#mindҳ
mind_downbutton = '//*[@resource-id="com.yiwuzhibo:id/tab_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]'
#ǩ����ť
mind_sign_in = '//android.widget.ScrollView/android.widget.ImageView[1]'
#ͷ���
mind_man_icon = '//android.widget.ScrollView/android.widget.ImageView[2]'

#��������
mind_people_center = '��������'
#��������
mind_people_data = '��������'
#�û�ͷ��
mind_people_icon_editor = '�༭'
#���
mind_people_photograph = '����'
#����button
mind_photograph_button = 'com.huawei.camera:id/place_holder_shutter_button'
#���ձ���
mind_photograph_done = 'com.huawei.camera:id/done_button'
#ȷ���滻��Ƭ
mind_menu_crop = 'com.yiwuzhibo:id/menu_crop'
#�༭���
mind_editor_done = '���'

#�ҵ��˻�
mind_my_account = '�ҵ��˻�'
#��������
mind_host_center = '��������'
#�ҵĵȼ�
mind_my_level = '�ҵĵȼ�'
#�ҵ�װ��
mind_my_dress = '�ҵ�װ��'
#С���̳�
mind_ele_mall = 'С���̳�'
#�ҵ���Ƶ
mind_my_video = '�ҵ���Ƶ'
#�ǳƿ�
mind_my_nickname_editor = '�����Զ�������, ����д'
#�Ա���
mind_sex = '�Ա�'
#�Ա�-��
mind_sex_man = '��'
#�Ա�-Ů
mind_sex_woman = 'Ů'
#�Ա�-������
mind_sex_unkown = '������'
#����/����
mind_countries = "����/����"
#����-������
mind_countries_Irish = '������'
#����-����
mind_countries_aman = '����'
#����
mind_city_editor = '//android.widget.ScrollView/android.widget.EditText[2]'
#����
mind_birthday_editor = '����'
#ȷ��
mind_birthday_determine = 'ȷ��'
#ְҵ
mind_professional_editor = '��ְҵ, ����д'
#����ǩ��
mind_signature_editor = 'û�и���ǩ��, ����һ������עĿ��ǩ����~'
#����ǩ��-mes
mind_signature_editor_mes = 'û�и���ǩ��'
#��ԭ����ǩ��
reduction_mind_signature_editor = 'û�и���ǩ��2, ����һ������עĿ��ǩ����~'
#�޸ĺ���ǳ�
mind_change_nickname = '��������, ����д'
#��ԭְҵ
reduction_mind_professional_editor = '����, ����д'
#�ҵ��˻�title
mind_tv_bar_title = 'com.yiwuzhibo:id/tv_bar_title'
#С���
mind_ele_coin = 'С���'
#��
mind_ele_bean = '��'
#С��ҿ�Ƭ
mind_ele_conin_bk = 'com.yiwuzhibo:id/ele_coin_bk'
#С���icon
mind_elecoin_icon = 'com.yiwuzhibo:id/elecoin_icon'
#С��ҽ��
mind_ele_coin_count = 'com.yiwuzhibo:id/ele_coin_count'
#С��ҳ�ֵ��ť
mind_elecoin_recharge = 'com.yiwuzhibo:id/elecoin_recharge'
#�󶹿�Ƭ
mind_ele_bean_bk = 'com.yiwuzhibo:id/ele_bean_bk'
#��icon
mind_elebean_icon = 'com.yiwuzhibo:id/elebean_icon'
#�����
mind_ele_bean_count = 'com.yiwuzhibo:id/ele_bean_count'
#�����tab
mind_elebean_packet = 'com.yiwuzhibo:id/elebean_packet'
#����ϸtab
mind_elebean_detail = 'com.yiwuzhibo:id/elebean_detail'
#�����title
mind_bean_gift_page_title = '�����'
#����ϸtitle
mind_bean_gift_page_detail = '����ϸ'
#��ֵС���title
mind_account_tv_bar_title = "com.yiwuzhibo:id/tv_bar_title"
#�û�ͷ��
mind_account_my_head="com.yiwuzhibo:id/my_head"
#�û��ǳ�
mind_account_nick_name="com.yiwuzhibo:id/nick_name"
#С���icon
mind_account_my_elecoin_icon="com.yiwuzhibo:id/my_elecoin_icon"
#С������
mind_account_my_elebean_title="com.yiwuzhibo:id/my_elebean_title"
#�û�ʵ��С������
mind_account_tv_balance="com.yiwuzhibo:id/tv_balance"
#��ѯ��ϸ
mind_account_tv_bar_right="com.yiwuzhibo:id/tv_bar_right"
#��ֵ��λ-1
mind_account_gear_01='//*[@resource-id="com.yiwuzhibo:id/rv_recharge"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
#֧����ʽ
mind_pay_type = 'com.yiwuzhibo:id/tv_item_pay_type'
#֧����ť
mind_bgv_pay = 'com.yiwuzhibo:id/bgv_pay'
#��ֵ����
mind_pay_amount = 'com.yiwuzhibo:id/tv_pay_amount'
#�����ϸtitle
mind_detail_page_title = '�����ϸ'
#������ϸtab
mind_income_detail_tab = '����� 1 ����ǩ���� 2 ��'
#֧����ϸtab
mind_spending_detail_tab = '֧���� 2 ����ǩ���� 2 ��'
#��������-�ҵ�����
mind_host_center_earnings = '�ҵ�����'
#���ּ�¼
mind_host_center_earnings_withdrawal_record = '���ּ�¼'
#��������-�ҵ�����
mind_host_center_everytoday_earnings = 'ÿ������'
#��������-�ҵ�����
mind_host_center_today_income = '��������'
#��������-�ҵ�����
mind_host_center_month_income = '��������'
#��������-�ҵ�����
mind_host_center_all_income = '�ܼ�����'
#ÿ������
#��������-ǩԼ����
mind_host_center_signing = 'ǩԼ����'
#��������-ֱ����¼
mind_host_center_record = 'ֱ����¼'
#��������-���װ�
mind_host_center_contribution = '���װ�'
#��������-��˿��
mind_host_center_fans = '��˿��'
#��������-�ҵĳɾ�
mind_host_center_achievement = '�ҵĳɾ�'
#��������-ֱ�������Ա
mind_host_center_administrator = 'ֱ�������Ա'
#��������-�������
mind_host_center_banned = '�������'


class Mind(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("�������mindҳ")
    def click_mind_button(self):
        self.base.click(mind_downbutton,mind_downbutton)

    @allure.step("�����������")
    def click_people_center(self):
        self.base.click(mind_downbutton,mind_downbutton)
        self.base.click_description(mind_people_center,mind_people_center)

    @allure.step('����������ҳ')
    def click_people_data(self):
        self.base.click(mind_downbutton,mind_downbutton)
        self.base.click_description(mind_people_center,mind_people_center)
        self.base.click_description(mind_people_data,mind_people_data)

    @allure.step('�滻�û�ͷ��')
    def change_people_icon(self):
        self.base.click_description(mind_people_icon_editor,mind_people_icon_editor)
        self.base.click_description(mind_people_photograph,mind_people_photograph)
        self.base.wait_time()
        self.base.click(mind_photograph_button,mind_photograph_button)
        self.base.click(mind_photograph_done,mind_photograph_done)
        self.base.click(mind_menu_crop,mind_menu_crop)
        self.base.wait_time(1)
        self.base.click_description(mind_editor_done,mind_editor_done)

    @allure.step('�����û�ͷ��ͼƬ')
    def save_element_pic(self,pic):
        self.base.wait_time(1)
        self.base.save_element_screenshot_description(r'D:\workspace_new\uiauto2_ele\aseert_pic\people_icon.jpg',mind_people_icon_editor,pic)

    @allure.step('�޸��ǳ�')
    def change_mind_nickname(self,nickname):
        self.base.set_text_contanis(mind_my_nickname_editor,nickname,mind_my_nickname_editor)
        self.base.back()

    @allure.step('�޸��Ա�')
    def change_mind_sex(self,sex):
        self.base.click_description_center(mind_sex)
        self.base.wait_time(1)
        if sex == '��':
            self.base.click_description(mind_sex_man,mind_sex_man)
        elif sex == 'Ů':
            self.base.click_description(mind_sex_woman,mind_sex_man)
        else:
            self.base.click_description(mind_sex_unkown,mind_sex_man)

    @allure.step('�޸Ĺ���/����-������')
    def change_mind_countries(self):
        self.base.click_description_center(mind_countries)
        self.base.wait_time()
        self.base.click_description(mind_countries_Irish,mind_countries_Irish)

    @allure.step('�޸Ĺ���/����-����')
    def change_mind_countries_aman(self):
        self.base.click_description_center(mind_countries)
        self.base.wait_time()
        self.base.click_description(mind_countries_aman,mind_countries_aman)

    @allure.step('�޸ĳ���')
    def change_mind_city(self,newCity):
        self.base.click(mind_city_editor,mind_city_editor)
        self.base.send_keys(mind_city_editor,newCity,mind_city_editor)
        self.base.back()

    @allure.step('�޸�����')
    def change_mind_birthday(self):
        self.base.click_description(mind_birthday_editor,mind_birthday_editor)
        self.base.click_description(mind_birthday_determine,mind_birthday_determine)

    @allure.step('ְҵ')
    def change_mind_professional(self,setProfessional):
        self.base.click(mind_professional_editor,mind_professional_editor)
        self.base.set_text_FastInputIME(setProfessional,setProfessional)

    @allure.step('����ǩ��')
    def change_mind_signature(self,new_signature):
        self.base.click(mind_signature_editor,mind_signature_editor)
        self.base.set_text_FastInputIME(new_signature,new_signature)

    @allure.step('����޸�')
    def editor_information_done(self):
        self.wait_time()
        self.base.click_description(mind_editor_done,mind_editor_done)

    @allure.step('�����û���Ϣ�޸ĳɹ�')
    def assert_host_information_change_success(self):
        self.base.assert_image_findit('./aseert_pic/change_people_countries.jpg')
        self.base.assert_image_findit('./aseert_pic/change_people_nickname.jpg')
        self.base.assert_image_findit('./aseert_pic/change_people_professional.jpg')
        self.base.assert_image_findit('./aseert_pic/change_people_sex.jpg')

    @allure.step('��ԭ��������')
    def reduction_mind_information(self,reduction_nickname):
        self.base.click_description(mind_people_center,mind_people_center)
        self.base.click_description(mind_people_data,mind_people_data)
        self.base.click(mind_change_nickname,mind_change_nickname)
        self.base.set_text_FastInputIME(reduction_nickname,reduction_nickname)
        self.change_mind_sex('������')
        self.change_mind_countries()
        self.base.click(reduction_mind_professional_editor,reduction_mind_professional_editor)
        self.base.set_text_FastInputIME('��ְҵ','��ְҵ')
        self.base.back()
        self.base.wait_time()
        self.base.swipe_up()
        self.base.click(reduction_mind_signature_editor,reduction_mind_signature_editor)
        self.base.set_text_FastInputIME(mind_signature_editor_mes,mind_signature_editor_mes)

    @allure.step('�����ҵ��˻�')
    def mind_account_tab(self):
        self.click_mind_button()
        self.base.click_description('�ҵ��˻�','�ҵ��˻�')

    @allure.step('����ҵ�С���')
    def mind_accout_elecoin(self):
        self.base.click(mind_ele_conin_bk,'С��ҿ�Ƭ')

    @allure.step('����󶹿�Ƭ')
    def mind_accout_elebean(self):
        self.base.click(mind_ele_bean_bk,'����󶹿�Ƭ')

    @allure.step('�����ҵ��˻����Ԫ�ش���')
    def assert_mind_account_element_exits(self):
        self.base.assert_element_exist(mind_tv_bar_title)
        self.base.assert_exist(mind_ele_coin)
        self.base.assert_exist(mind_ele_bean)
        self.base.assert_element_exist(mind_ele_coin_count)
        self.base.assert_element_exist(mind_ele_bean_count)
        self.base.assert_element_exist(mind_elecoin_recharge)

    @allure.step('���С��ҿ�Ƭ')
    def click_ele_conin_bk(self):
        self.base.click(mind_ele_conin_bk,'С��ҳ�ֵ��Ƭ')

    @allure.step('����󶹿�Ƭ')
    def click_ele_bean_bk(self):
        self.base.click(mind_ele_conin_bk,'�󶹿�Ƭ')

    @allure.step('����С��ҳ�ֵҳ��')
    def assert_ele_conin_page(self):
        self.base.assert_element_exist(mind_account_tv_bar_title)
        self.base.assert_element_exist(mind_account_my_head)
        self.base.assert_element_exist(mind_account_nick_name)
        self.base.assert_element_exist(mind_account_my_elecoin_icon)
        self.base.assert_element_exist(mind_account_my_elebean_title)
        self.base.assert_element_exist(mind_account_tv_balance)
        self.base.assert_element_exist(mind_account_tv_bar_right)

    @allure.step('���С��ҳ�ֵ��λ1')
    def click_mind_account_gear_01(self):
        self.base.click(mind_account_gear_01,'��ֵ��λ1-60С���')

    @allure.step('���Գ�ֵҳ��')
    def assert_account_gear_page(self):
        self.base.assert_element_exist(mind_pay_type)
        self.base.assert_element_exist(mind_bgv_pay)
        self.base.assert_element_exist(mind_pay_amount)

    @allure.step('�����ѯ��ϸ')
    def click_mind_account_tv_bar_right(self):
        self.base.click(mind_account_tv_bar_right,'��ѯ��ϸ')

    @allure.step('����С��������ϸ����չʾ����')
    def assert_account_eleconin_detail(self):
        self.base.assert_element_description_exist(mind_detail_page_title)
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_income.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_spending.jpg')

    @allure.step('��������tab')
    def click_mind_elebean_packet(self):
        self.base.click(mind_elebean_packet,'�����tab')

    @allure.step('�������ϸtab')
    def click_mind_elebean_detail(self):
        self.base.click(mind_elebean_detail,'����ϸtab')

    @allure.step('���������')
    def assert_mind_bean_gift_page(self):
        self.base.assert_element_description_exist(mind_bean_gift_page_title)
        self.base.assert_image_findit('./aseert_pic/mind_account_bean_gift_received.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_account_bean_gift_Sendout.jpg')

    @allure.step('���������')
    def assert_mind_bean_detail_page(self):
        self.base.assert_element_description_exist(mind_bean_gift_page_detail)
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_income.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_spending.jpg')

    @allure.step('������������')
    def click_mind_host_center(self):
        self.click_mind_button()
        self.base.click_description(mind_host_center,mind_host_center)

    @allure.step('������������-�ҵ�����')
    def click_mind_host_center_my_earnings(self):
        self.click_mind_host_center()
        self.base.click_description(mind_host_center_earnings,mind_host_center_earnings)

    @allure.step('�����ҵ�����ҳ��չʾ����')
    def assert_mind_my_earnings(self):
        self.base.assert_element_description_exist(mind_host_center_earnings_withdrawal_record)
        self.base.assert_element_description_exist(mind_host_center_earnings)
        self.base.assert_element_description_exist(mind_host_center_today_income)
        self.base.assert_element_description_exist(mind_host_center_month_income)
        self.base.assert_element_description_exist(mind_host_center_all_income)
