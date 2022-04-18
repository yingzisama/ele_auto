# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#ֱ����ť
iv_create = 'com.yiwuzhibo:id/iv_create' 
#��ֱͨ��
tiv_live = 'com.yiwuzhibo:id/tiv_live'
#��ʼֱ��
preview_start = 'com.yiwuzhibo:id/preview_start'
#�ر�ֱ��
av_room_top_close = 'com.yiwuzhibo:id/av_room_top_close'
#����ֱ��
close_live = '����ֱ��'
#����ͷ��
user_avatar = 'com.yiwuzhibo:id/user_avatar'
#��˿��
liveroom_play_fans_group = 'com.yiwuzhibo:id/liveroom_play_fans_group'
#��˿��
rly_fans_top3 = 'com.yiwuzhibo:id/rly_fans_top3'
#������
bgv_streamer_ranking = 'com.yiwuzhibo:id/bgv_streamer_ranking'
#���԰�ť
liveroom_comment = 'com.yiwuzhibo:id/liveroom_comment'
#���Կ�
input_edit_text_view = 'com.yiwuzhibo:id/input_edit_text_view'
#����
input_confirm_tv = 'com.yiwuzhibo:id/input_confirm_tv'
#���ð�ť
liveroom_fun_more = 'com.yiwuzhibo:id/liveroom_fun_more'
#������1
liveroom_button_1 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
#������1
liveroom_button_2 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
#������1
liveroom_button_3 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]'
#������1
liveroom_button_4 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[4]/android.widget.ImageView[1]'
#������1
liveroom_button_5 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[5]/android.widget.ImageView[1]'
#������1
liveroom_button_6 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[6]/android.widget.ImageView[1]'
#������1
liveroom_button_7 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[7]/android.widget.ImageView[1]'
#������1
liveroom_button_8 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[8]/android.widget.ImageView[1]'
#wx����
liveroom_share_wx = '΢��'
#����Ȧ����
liveroom_share_Circlefriends = '����Ȧ'
#Facebook����
liveroom_share_Facebook= 'Facebook'
#Twitter����
liveroom_share_Twitter = 'Twitter'
#Line����
liveroom_share_Line = 'Line'
#״̬��
sb_shape_default = 'com.yiwuzhibo:id/sb_shape_default'
#״ֵ̬
sb_progress_tv = 'com.yiwuzhibo:id/sb_progress_tv'
#ĥƤ
buffing_live = 'ĥƤ'
#����
whitening_live = '����'
#����
ruddy_live = '����'
#����tab
cb_shape = 'com.yiwuzhibo:id/cb_shape'
#����
big_eye = '����'
#����
thin_face = '����'
#�°�
chin_face = '�°�'
#��ͷ
forehead_face = '��ͷ'
#�ݱ�
nose_face = '�ݱ�'
#����
mouth_face = '����'

class Host(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("����ֱ����")
    def start_live(self):
        self.base.click(iv_create,iv_create)
        self.base.wait_element_appear(tiv_live,tiv_live,1)
        self.base.click(tiv_live,tiv_live)
        self.base.click(preview_start,preview_start)
        self.base.wait_time()

    @allure.step("�ر�ֱ����")
    def close_liveroom(self):
        self.base.click(av_room_top_close,av_room_top_close)
        self.base.wait_element_appear(close_live,close_live,1)
        self.base.click(close_live,av_room_top_close)

    @allure.step("�������ͷ��")
    def click_user_avatar(self):
        self.base.click(user_avatar,user_avatar)

    @allure.step("�����˿��")
    def click_fans_group(self):
        self.base.click(liveroom_play_fans_group,liveroom_play_fans_group)

    @allure.step("�鿴��˿��")
    def my_fans_ranktop(self):
        self.base.click(liveroom_play_fans_group,liveroom_play_fans_group)
        self.base.click(rly_fans_top3,rly_fans_top3)

    @allure.step("�鿴������")
    def my_streamer_ranking(self):
        self.base.click(liveroom_play_fans_group,liveroom_play_fans_group)
        self.base.click(bgv_streamer_ranking,bgv_streamer_ranking)

    @allure.step("��Ļ����")
    def my_input_comment(self,input_message):
        self.base.click(liveroom_comment,liveroom_comment)
        self.base.send_keys(input_edit_text_view,input_message,input_edit_text_view)
        self.base.click(input_confirm_tv,input_confirm_tv)

    @allure.step("��������")
    def click_liveroom_fun_more(self):
        self.base.click(liveroom_fun_more,liveroom_fun_more)

    @allure.step("�ײ����󻬶�")
    def swipe_downtools_left(self):
        self.base.swipe_x1y1x2y2(0.882, 0.869,0.179, 0.869)
        self.base.wait_time(1)

    @allure.step("���tools ��һ��button")
    def click_liveroom_tools_button_1(self):
        self.base.click(liveroom_button_1,liveroom_button_1)

    @allure.step("�������-����")
    def click_liveroom_tools_beauty_face(self):
        self.base.click(liveroom_fun_more,liveroom_fun_more)
        self.base.click(liveroom_button_1,liveroom_button_1)

    @allure.step("�������-����")
    def click_liveroom_tools_share(self):
        self.base.click(liveroom_fun_more,liveroom_fun_more)
        self.base.swipe_x1y1x2y2(0.882, 0.869,0.179, 0.869)
        self.base.wait_time(1)
        self.base.click(liveroom_button_1,liveroom_button_1)

    @allure.step("���tools ������ĸ�button-����")
    def click_liveroom_tools_button_4(self):
        self.base.click(liveroom_button_4,liveroom_button_4)

    @allure.step("΢�ŷ���")
    def click_liveroom_share_wx(self):
        self.base.click(liveroom_share_wx,liveroom_share_wx)

    @allure.step("����Ȧ����")
    def click_liveroom_share_Circlefriends(self):
        self.base.click(liveroom_share_Circlefriends,liveroom_share_Circlefriends)

    @allure.step("Facebook����")
    def click_liveroom_share_Facebook(self):
        self.base.click(liveroom_share_Facebook,liveroom_share_Facebook)

    @allure.step("Twitter����")
    def click_liveroom_share_Twitter(self):
        self.base.click(liveroom_share_Twitter,liveroom_share_Twitter)

    @allure.step("Line����")
    def click_liveroom_share_Line(self):
        self.base.click(liveroom_share_Line,liveroom_share_Line)

    @allure.step('�������м�����')
    def live_swipe_shape_left(self):
        self.base.swipe_x1y1x2y2(0.5, 0.918,0.091, 0.919)

    @allure.step('������������һ�')
    def live_swipe_shape_right(self):
        self.base.swipe_x1y1x2y2(0.091, 0.919,0.921, 0.919)

    @allure.step('�жϽ�����ֵΪ0')
    def live_get_swipe_value_0(self):
        value = self.base.get_element_text(sb_progress_tv)
        assert value == '0'

    @allure.step('�жϽ�����ֵΪ100')
    def live_get_swipe_value_100(self):
        value = self.base.get_element_text(sb_progress_tv)
        assert value == '100'

    @allure.step('����������')
    def live_assert_swipe_value(self):
        self.live_swipe_shape_left()
        self.live_get_swipe_value_0()
        self.live_swipe_shape_right()
        self.live_get_swipe_value_100()

    @allure.step('���face tab')
    def live_click_cb_shape(self):
        self.base.click(cb_shape,cb_shape)

    @allure.step('�������')
    def live_click_big_eye(self):
        self.base.click(big_eye,big_eye)

    @allure.step('�������')
    def live_click_thin_face(self):
        self.base.click(thin_face,thin_face)

    @allure.step('����°�')
    def live_click_chin_face(self):
        self.base.click(chin_face,chin_face)

    @allure.step('�����ͷ')
    def live_click_forehead_face(self):
        self.base.click(forehead_face,forehead_face)

    @allure.step('����ݱ�')
    def live_click_nose_face(self):
        self.base.click(nose_face,nose_face)

    @allure.step('�������')
    def live_click_mouth_face(self):
        self.base.click(mouth_face,mouth_face)

    @allure.step('�������')
    def live_click_whitening(self):
        self.base.click(whitening_live,whitening_live)

    @allure.step('�������')
    def live_click_ruddy(self):
        self.base.click(ruddy_live,ruddy_live)
