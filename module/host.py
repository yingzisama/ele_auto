# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#直播按钮
iv_create = 'com.yiwuzhibo:id/iv_create' 
#普通直播
tiv_live = 'com.yiwuzhibo:id/tiv_live'
#开始直播
preview_start = 'com.yiwuzhibo:id/preview_start'
#关闭直播
av_room_top_close = 'com.yiwuzhibo:id/av_room_top_close'
#结束直播
close_live = '结束直播'
#主播头像
user_avatar = 'com.yiwuzhibo:id/user_avatar'
#粉丝团
liveroom_play_fans_group = 'com.yiwuzhibo:id/liveroom_play_fans_group'
#粉丝榜
rly_fans_top3 = 'com.yiwuzhibo:id/rly_fans_top3'
#主播榜
bgv_streamer_ranking = 'com.yiwuzhibo:id/bgv_streamer_ranking'
#发言按钮
liveroom_comment = 'com.yiwuzhibo:id/liveroom_comment'
#发言框
input_edit_text_view = 'com.yiwuzhibo:id/input_edit_text_view'
#发送
input_confirm_tv = 'com.yiwuzhibo:id/input_confirm_tv'
#设置按钮
liveroom_fun_more = 'com.yiwuzhibo:id/liveroom_fun_more'
#设置栏1
liveroom_button_1 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_2 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_3 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_4 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[4]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_5 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[5]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_6 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[6]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_7 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[7]/android.widget.ImageView[1]'
#设置栏1
liveroom_button_8 = '//*[@resource-id="com.yiwuzhibo:id/av_room_fun_rv"]/android.widget.LinearLayout[8]/android.widget.ImageView[1]'
#wx分享
liveroom_share_wx = '微信'
#朋友圈分享
liveroom_share_Circlefriends = '朋友圈'
#Facebook分享
liveroom_share_Facebook= 'Facebook'
#Twitter分享
liveroom_share_Twitter = 'Twitter'
#Line分享
liveroom_share_Line = 'Line'
#状态条
sb_shape_default = 'com.yiwuzhibo:id/sb_shape_default'
#状态值
sb_progress_tv = 'com.yiwuzhibo:id/sb_progress_tv'
#磨皮
buffing_live = '磨皮'
#美白
whitening_live = '美白'
#红润
ruddy_live = '红润'
#脸型tab
cb_shape = 'com.yiwuzhibo:id/cb_shape'
#大眼
big_eye = '大眼'
#瘦脸
thin_face = '瘦脸'
#下巴
chin_face = '下巴'
#额头
forehead_face = '额头'
#瘦鼻
nose_face = '瘦鼻'
#嘴型
mouth_face = '嘴型'

class Host(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("创建直播间")
    def start_live(self):
        self.base.click(iv_create,iv_create)
        self.base.wait_element_appear(tiv_live,tiv_live,1)
        self.base.click(tiv_live,tiv_live)
        self.base.click(preview_start,preview_start)
        self.base.wait_time()

    @allure.step("关闭直播间")
    def close_liveroom(self):
        self.base.click(av_room_top_close,av_room_top_close)
        self.base.wait_element_appear(close_live,close_live,1)
        self.base.click(close_live,av_room_top_close)

    @allure.step("点击主播头像")
    def click_user_avatar(self):
        self.base.click(user_avatar,user_avatar)

    @allure.step("点击粉丝团")
    def click_fans_group(self):
        self.base.click(liveroom_play_fans_group,liveroom_play_fans_group)

    @allure.step("查看粉丝榜")
    def my_fans_ranktop(self):
        self.base.click(liveroom_play_fans_group,liveroom_play_fans_group)
        self.base.click(rly_fans_top3,rly_fans_top3)

    @allure.step("查看主播榜")
    def my_streamer_ranking(self):
        self.base.click(liveroom_play_fans_group,liveroom_play_fans_group)
        self.base.click(bgv_streamer_ranking,bgv_streamer_ranking)

    @allure.step("弹幕发言")
    def my_input_comment(self,input_message):
        self.base.click(liveroom_comment,liveroom_comment)
        self.base.send_keys(input_edit_text_view,input_message,input_edit_text_view)
        self.base.click(input_confirm_tv,input_confirm_tv)

    @allure.step("打开设置栏")
    def click_liveroom_fun_more(self):
        self.base.click(liveroom_fun_more,liveroom_fun_more)

    @allure.step("底部栏左滑动")
    def swipe_downtools_left(self):
        self.base.swipe_x1y1x2y2(0.882, 0.869,0.179, 0.869)
        self.base.wait_time(1)

    @allure.step("点击tools 第一个button")
    def click_liveroom_tools_button_1(self):
        self.base.click(liveroom_button_1,liveroom_button_1)

    @allure.step("点击设置-美颜")
    def click_liveroom_tools_beauty_face(self):
        self.base.click(liveroom_fun_more,liveroom_fun_more)
        self.base.click(liveroom_button_1,liveroom_button_1)

    @allure.step("点击设置-分享")
    def click_liveroom_tools_share(self):
        self.base.click(liveroom_fun_more,liveroom_fun_more)
        self.base.swipe_x1y1x2y2(0.882, 0.869,0.179, 0.869)
        self.base.wait_time(1)
        self.base.click(liveroom_button_1,liveroom_button_1)

    @allure.step("点击tools 点击第四个button-静音")
    def click_liveroom_tools_button_4(self):
        self.base.click(liveroom_button_4,liveroom_button_4)

    @allure.step("微信分享")
    def click_liveroom_share_wx(self):
        self.base.click(liveroom_share_wx,liveroom_share_wx)

    @allure.step("朋友圈分享")
    def click_liveroom_share_Circlefriends(self):
        self.base.click(liveroom_share_Circlefriends,liveroom_share_Circlefriends)

    @allure.step("Facebook分享")
    def click_liveroom_share_Facebook(self):
        self.base.click(liveroom_share_Facebook,liveroom_share_Facebook)

    @allure.step("Twitter分享")
    def click_liveroom_share_Twitter(self):
        self.base.click(liveroom_share_Twitter,liveroom_share_Twitter)

    @allure.step("Line分享")
    def click_liveroom_share_Line(self):
        self.base.click(liveroom_share_Line,liveroom_share_Line)

    @allure.step('进度条中间向左滑')
    def live_swipe_shape_left(self):
        self.base.swipe_x1y1x2y2(0.5, 0.918,0.091, 0.919)

    @allure.step('进度条左边向右滑')
    def live_swipe_shape_right(self):
        self.base.swipe_x1y1x2y2(0.091, 0.919,0.921, 0.919)

    @allure.step('判断进度条值为0')
    def live_get_swipe_value_0(self):
        value = self.base.get_element_text(sb_progress_tv)
        assert value == '0'

    @allure.step('判断进度条值为100')
    def live_get_swipe_value_100(self):
        value = self.base.get_element_text(sb_progress_tv)
        assert value == '100'

    @allure.step('滑动进度条')
    def live_assert_swipe_value(self):
        self.live_swipe_shape_left()
        self.live_get_swipe_value_0()
        self.live_swipe_shape_right()
        self.live_get_swipe_value_100()

    @allure.step('点击face tab')
    def live_click_cb_shape(self):
        self.base.click(cb_shape,cb_shape)

    @allure.step('点击大眼')
    def live_click_big_eye(self):
        self.base.click(big_eye,big_eye)

    @allure.step('点击瘦脸')
    def live_click_thin_face(self):
        self.base.click(thin_face,thin_face)

    @allure.step('点击下巴')
    def live_click_chin_face(self):
        self.base.click(chin_face,chin_face)

    @allure.step('点击额头')
    def live_click_forehead_face(self):
        self.base.click(forehead_face,forehead_face)

    @allure.step('点击瘦鼻')
    def live_click_nose_face(self):
        self.base.click(nose_face,nose_face)

    @allure.step('点击嘴型')
    def live_click_mouth_face(self):
        self.base.click(mouth_face,mouth_face)

    @allure.step('点击美白')
    def live_click_whitening(self):
        self.base.click(whitening_live,whitening_live)

    @allure.step('点击红润')
    def live_click_ruddy(self):
        self.base.click(ruddy_live,ruddy_live)
