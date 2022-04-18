# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#ֱ����ť
iv_create = 'com.yiwuzhibo:id/iv_create' 

#��ֱͨ��
tiv_live = 'com.yiwuzhibo:id/tiv_live'
#OBSֱ��
tiv_obs_live = 'com.yiwuzhibo:id/tiv_obs_live'

#��������
av_preview_cover_bg = 'com.yiwuzhibo:id/av_preview_cover_bg'
#ֱ������
av_preview_edit_room_title = 'com.yiwuzhibo:id/av_preview_edit_room_title'
#΢�ŷ���
preview_share_wx_friend = 'com.yiwuzhibo:id/preview_share_wx_friend'
#����Ȧ����
preview_share_wx_circle = 'com.yiwuzhibo:id/preview_share_wx_circle'
#facebook����
preview_share_facebook = 'com.yiwuzhibo:id/preview_share_facebook'
#���ط���
preview_share_twitter = 'com.yiwuzhibo:id/preview_share_twitter'
#line����
preview_share_line = 'com.yiwuzhibo:id/preview_share_line'

#��ͷ��ת
preview_switch_camera_tv = 'com.yiwuzhibo:id/preview_switch_camera_tv'
#���հ�ť
preview_filter_tv = 'com.yiwuzhibo:id/preview_filter_tv'
#��ʼֱ��
preview_start = 'com.yiwuzhibo:id/preview_start'

#��ӷ���
cover_add = 'com.yiwuzhibo:id/cover_add'
#���
photo_album = '//*[@text="���"]'
#�����
camera_photo = '���'
#��һ��ͼƬ
first_pic_camera = '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]'
#ѡ����Ƭ-ȷ��
pic_select_confirm = 'com.hihonor.photos:id/head_select_right'
#ʹ��
select_pic_use = 'com.yiwuzhibo:id/activity_crop_photo_confirm'
#�����
cover_status_tv = '�����'
#����ɾ��
cover_delete_click = 'com.yiwuzhibo:id/cover_delete_click'
#ɾ��ȷ��
tv_comfirm = "ȷ��"

#����tab
cb_color = 'com.yiwuzhibo:id/cb_color'
#ĥƤ
buffing_live = 'ĥƤ'
#����
whitening_live = '����'
#����
ruddy_live = '����'
#״̬��
sb_shape_default = 'com.yiwuzhibo:id/sb_shape_default'
#״ֵ̬
sb_progress_tv = 'com.yiwuzhibo:id/sb_progress_tv'

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

#�˾�tab
cb_filter = 'com.yiwuzhibo:id/cb_filter'
#ԭͼ
rv_filter_01 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'
#�ͷ�
rv_filter_02 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]'
#����
rv_filter_03 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]'
#���
rv_filter_04 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[4]/android.widget.FrameLayout[1]'
#��ϵ
rv_filter_05 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[5]/android.widget.FrameLayout[1]'
#����
rv_filter_06 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[6]/android.widget.FrameLayout[1]'


class Live(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    #����ֱ��׼���׶�
    @allure.step("����ֱ��׼���׶�")
    def start_live_prepare(self):
        self.base.click(iv_create,iv_create)
        self.base.wait_element_appear(tiv_live,tiv_live,1)
        self.base.click(tiv_live,tiv_live)

    @allure.step("����ֱ����")
    def start_live(self):
        self.base.click(iv_create,iv_create)
        self.base.wait_element_appear(tiv_live,tiv_live,1)
        self.base.click(tiv_live,tiv_live)
        self.base.click(preview_start,preview_start)
        self.base.wait_time()
        self.base.assert_exist('��˿��')

    @allure.step("����ֱ�������")
    def start_live_set_title(self,titleName):
        self.base.send_keys(av_preview_edit_room_title,titleName,av_preview_edit_room_title)
        self.base.back()

    @allure.step("����ֱ��")
    def start_live_true(self):
        self.base.click(preview_start,preview_start)

    @allure.step("ѡ�����")
    def choose_cover(self):
        self.base.click(av_preview_cover_bg,av_preview_cover_bg)
        self.base.click(cover_add,cover_add)

    @allure.step("�������һ��")
    def add_first_camera(self):
        self.base.click(photo_album,photo_album)
        self.base.click(camera_photo,camera_photo)
        self.base.click(first_pic_camera,first_pic_camera)
        self.base.click(pic_select_confirm,pic_select_confirm)
        self.base.click(select_pic_use,select_pic_use)

    @allure.step("ɾ����ǰֱ������ͼƬ")
    def cover_delete(self):
        self.base.click(cover_delete_click,cover_delete_click)
        self.base.click(tv_comfirm,tv_comfirm)

    @allure.step("΢�ŷ���")
    def live_share_wx(self):
        self.base.click(preview_share_wx_friend,preview_share_wx_friend)

    @allure.step("����Ȧ����")
    def live_share_wx_circle(self):
        self.base.click(preview_share_wx_circle,preview_share_wx_circle)

    @allure.step("facebook����")
    def live_share_facebook(self):
        self.base.click(preview_share_facebook,preview_share_facebook)

    @allure.step("twitter����")
    def live_share_twitter(self):
        self.base.click(preview_share_twitter,preview_share_twitter)

    @allure.step("line����")
    def live_share_line(self):
        self.base.click(preview_share_line,preview_share_line)

    @allure.step('����������')
    def live_beauty_face_tools(self):
        self.base.click(preview_filter_tv,preview_filter_tv)

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

    @allure.step('���ĥƤ')
    def live_click_buffing(self):
        self.base.click(buffing_live,buffing_live)

    @allure.step('�������')
    def live_click_whitening(self):
        self.base.click(whitening_live,whitening_live)

    @allure.step('�������')
    def live_click_ruddy(self):
        self.base.click(ruddy_live,ruddy_live)

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

    @allure.step('����������')
    def live_assert_swipe_value(self):
        self.live_swipe_shape_left()
        self.live_get_swipe_value_0()
        self.live_swipe_shape_right()
        self.live_get_swipe_value_100()
