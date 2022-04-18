# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#������ť
ele_iv_search = 'com.yiwuzhibo:id/iv_search'
#������
ele_et_search = 'com.yiwuzhibo:id/et_search'
#��������
ele_host_name = '�Զ�������������'
#������ť
ele_btn_search = 'com.yiwuzhibo:id/btn_search'
#�����ǳ�
ele_liveroom_streamer_name = 'com.yiwuzhibo:id/liveroom_streamer_name'
#����ͷ��
ele_user_avatar = 'com.yiwuzhibo:id/user_avatar'
#�α�ϯ
ele_visitor_avatar = 'com.yiwuzhibo:id/visitor_avatar'
#��˿��
ele_live_room_top_fans_tv = 'com.yiwuzhibo:id/live_room_top_fans_tv'
#���װ�
ele_contribute_tv = 'com.yiwuzhibo:id/contribute_tv'
#�����
ele_liveroom_im_list = 'com.yiwuzhibo:id/liveroom_im_list'
#���԰�ť
ele_liveroom_play_comment = 'com.yiwuzhibo:id/liveroom_play_comment'
#����ť
ele_liveroom_play_link_mic = 'com.yiwuzhibo:id/liveroom_play_link_mic'
#����ť
ele_liveroom_play_share = 'com.yiwuzhibo:id/liveroom_play_share'
#��Ϣ��ť
ele_liveroom_play_private_chat = 'com.yiwuzhibo:id/liveroom_play_private_chat'
#���ఴť
ele_liveroom_play_fun_more = 'com.yiwuzhibo:id/liveroom_play_fun_more'
#���ﰴť
ele_liveroom_play_gift = 'com.yiwuzhibo:id/liveroom_play_gift'
#�˳���ť
ele_av_room_top_close = 'com.yiwuzhibo:id/av_room_top_close'

#������Ϣ��Ƭ-����ͷ��
ele_hostcard_user_avatar = 'com.yiwuzhibo:id/user_avatar'
#������Ϣ��Ƭ-�����ǳ�
ele_hostcard_nickname = 'com.yiwuzhibo:id/av_room_person_name'
#������Ϣ��Ƭ-С���
ele_hostcard_uid = 'com.yiwuzhibo:id/ll_room_person_uid'
#������Ϣ��Ƭ-���ఴť
ele_hostcard_more = 'com.yiwuzhibo:id/av_room_person_manager'
#������Ϣ��Ƭ-�ٱ�
ele_hostcard_report = 'com.yiwuzhibo:id/av_room_person_report'
#������Ϣ��Ƭ-�û��ȼ�
ele_hostcard_level = 'com.yiwuzhibo:id/av_room_person_tag'
#������Ϣ��Ƭ-����ǩ��
ele_hostcard_sign = 'com.yiwuzhibo:id/av_room_person_sign'
#������Ϣ��Ƭ-��˿��
ele_hostcard_fans = 'com.yiwuzhibo:id/av_room_person_detail_fans'
#������Ϣ��Ƭ-��ע��
ele_hostcard_follower = 'com.yiwuzhibo:id/av_room_person_detail_follower'
#������Ϣ��Ƭ-�ͳ���
ele_hostcard_send = 'com.yiwuzhibo:id/av_room_person_detail_send'
#������Ϣ��Ƭ-�յ���
ele_hostcard_get = 'com.yiwuzhibo:id/av_room_person_detail_get'
#������Ϣ��Ƭ-��ҳ
ele_hostcard_homepage = 'com.yiwuzhibo:id/av_room_person_detail_main'
#������Ϣ��Ƭ-@
ele_hostcard_eit = 'com.yiwuzhibo:id/av_room_person_detail_at'
#������Ϣ��Ƭ-��ע
ele_hostcard_focus = 'com.yiwuzhibo:id/av_room_person_detail_focus'
#������Ϣ��Ƭ-����
ele_hostcard_friend_status = 'com.yiwuzhibo:id/av_room_friend_status'

class Audience(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("����ֱ����")
    def enter_live_room(self):
        self.base.click(ele_iv_search,'������ť')
        self.base.send_keys(ele_et_search,'�Զ�������','������������-�Զ�������')
        self.base.click(ele_btn_search,'������ť')
        self.base.click(ele_host_name,'���ֱ����')

    @allure.step('����ֱ������ڶ˽�������չʾ')
    def assert_live_room_element(self):
        #����ֱ���������ǳƴ���
        self.base.assert_element_exist(ele_liveroom_streamer_name)
        #����ֱ��������ͷ�����
        self.base.assert_element_exist(ele_user_avatar)
        #����ֱ����α�ϯ����
        self.base.assert_element_exist(ele_visitor_avatar)
        #����ֱ�����˿�Ŵ���
        self.base.assert_element_exist(ele_live_room_top_fans_tv)
        #����ֱ���乱�װ����
        self.base.assert_element_exist(ele_contribute_tv)
        #����ֱ������������
        self.base.assert_element_exist(ele_liveroom_im_list)
        #����ֱ���䷢�԰�ť����
        self.base.assert_element_exist(ele_liveroom_play_comment)
        #����ֱ��������ť����
        self.base.assert_element_exist(ele_liveroom_play_link_mic)
        #����ֱ�������ť����
        self.base.assert_element_exist(ele_liveroom_play_share)
        #����ֱ������Ϣ��ť����
        self.base.assert_element_exist(ele_liveroom_play_private_chat)
        #����ֱ������ఴť����
        self.base.assert_element_exist(ele_liveroom_play_fun_more)
        #����ֱ�������ﰴť����
        self.base.assert_element_exist(ele_liveroom_play_gift)
        #����ֱ����رհ�ť����
        self.base.assert_element_exist(ele_av_room_top_close)

    @allure.step('�������ͷ��')
    def click_ele_user_avatar(self):
        self.base.click(ele_user_avatar,'����ͷ��')

    @allure.step('����������Ϣ��Ƭ����Ԫ��')
    def assert_host_layout_bg(self):
        #����������Ϣ��Ƭ����ͷ�����
        self.base.assert_element_exist(ele_hostcard_user_avatar)
        #����������Ϣ��Ƭ�����ǳƴ���
        self.base.assert_element_exist(ele_hostcard_nickname)
        #����������Ϣ��ƬС��Ŵ���
        self.base.assert_element_exist(ele_hostcard_uid)
        #����������Ϣ��Ƭ���ఴť����
        self.base.assert_element_exist(ele_hostcard_more)
        #����������Ϣ��Ƭ�ٱ���ť����
        self.base.assert_element_exist(ele_hostcard_report)
        #����������Ϣ��Ƭ�û��ȼ�����
        self.base.assert_element_exist(ele_hostcard_level)
        #����������Ϣ��Ƭ����ǩ������
        self.base.assert_element_exist(ele_hostcard_sign)
        #����������Ϣ��Ƭ��˿������
        self.base.assert_element_exist(ele_hostcard_fans)
        #����������Ϣ��Ƭ��ע������
        self.base.assert_element_exist(ele_hostcard_follower)
        #����������Ϣ��Ƭ�ͳ�������
        self.base.assert_element_exist(ele_hostcard_send)
        #����������Ϣ��Ƭ�յ�������
        self.base.assert_element_exist(ele_hostcard_get)
        #����������Ϣ��Ƭ��ҳ��ť����
        self.base.assert_element_exist(ele_hostcard_homepage)
        #����������Ϣ��Ƭ@��ť����
        self.base.assert_element_exist(ele_hostcard_eit)
        #����������Ϣ��Ƭ��ע����
        self.base.assert_element_exist(ele_hostcard_focus)
        #����������Ϣ��Ƭ���Ѵ���
        self.base.assert_element_exist(ele_hostcard_friend_status)

    @allure.step('���������������ҳ')
    def click_hostcard_homepage(self):
        self.base.click(ele_hostcard_homepage,'��ҳ��ť')
