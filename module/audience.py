# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#搜索按钮
ele_iv_search = 'com.yiwuzhibo:id/iv_search'
#搜索框
ele_et_search = 'com.yiwuzhibo:id/et_search'
#主播名字
ele_host_name = '自动化测试主播端'
#搜索按钮
ele_btn_search = 'com.yiwuzhibo:id/btn_search'
#主播昵称
ele_liveroom_streamer_name = 'com.yiwuzhibo:id/liveroom_streamer_name'
#主播头像
ele_user_avatar = 'com.yiwuzhibo:id/user_avatar'
#嘉宾席
ele_visitor_avatar = 'com.yiwuzhibo:id/visitor_avatar'
#粉丝团
ele_live_room_top_fans_tv = 'com.yiwuzhibo:id/live_room_top_fans_tv'
#贡献榜
ele_contribute_tv = 'com.yiwuzhibo:id/contribute_tv'
#聊天框
ele_liveroom_im_list = 'com.yiwuzhibo:id/liveroom_im_list'
#发言按钮
ele_liveroom_play_comment = 'com.yiwuzhibo:id/liveroom_play_comment'
#连麦按钮
ele_liveroom_play_link_mic = 'com.yiwuzhibo:id/liveroom_play_link_mic'
#分享按钮
ele_liveroom_play_share = 'com.yiwuzhibo:id/liveroom_play_share'
#消息按钮
ele_liveroom_play_private_chat = 'com.yiwuzhibo:id/liveroom_play_private_chat'
#更多按钮
ele_liveroom_play_fun_more = 'com.yiwuzhibo:id/liveroom_play_fun_more'
#礼物按钮
ele_liveroom_play_gift = 'com.yiwuzhibo:id/liveroom_play_gift'
#退出按钮
ele_av_room_top_close = 'com.yiwuzhibo:id/av_room_top_close'

#主播信息卡片-主播头像
ele_hostcard_user_avatar = 'com.yiwuzhibo:id/user_avatar'
#主播信息卡片-主播昵称
ele_hostcard_nickname = 'com.yiwuzhibo:id/av_room_person_name'
#主播信息卡片-小象号
ele_hostcard_uid = 'com.yiwuzhibo:id/ll_room_person_uid'
#主播信息卡片-更多按钮
ele_hostcard_more = 'com.yiwuzhibo:id/av_room_person_manager'
#主播信息卡片-举报
ele_hostcard_report = 'com.yiwuzhibo:id/av_room_person_report'
#主播信息卡片-用户等级
ele_hostcard_level = 'com.yiwuzhibo:id/av_room_person_tag'
#主播信息卡片-个人签名
ele_hostcard_sign = 'com.yiwuzhibo:id/av_room_person_sign'
#主播信息卡片-粉丝数
ele_hostcard_fans = 'com.yiwuzhibo:id/av_room_person_detail_fans'
#主播信息卡片-关注数
ele_hostcard_follower = 'com.yiwuzhibo:id/av_room_person_detail_follower'
#主播信息卡片-送出数
ele_hostcard_send = 'com.yiwuzhibo:id/av_room_person_detail_send'
#主播信息卡片-收到数
ele_hostcard_get = 'com.yiwuzhibo:id/av_room_person_detail_get'
#主播信息卡片-主页
ele_hostcard_homepage = 'com.yiwuzhibo:id/av_room_person_detail_main'
#主播信息卡片-@
ele_hostcard_eit = 'com.yiwuzhibo:id/av_room_person_detail_at'
#主播信息卡片-关注
ele_hostcard_focus = 'com.yiwuzhibo:id/av_room_person_detail_focus'
#主播信息卡片-好友
ele_hostcard_friend_status = 'com.yiwuzhibo:id/av_room_friend_status'

class Audience(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("进入直播间")
    def enter_live_room(self):
        self.base.click(ele_iv_search,'搜索按钮')
        self.base.send_keys(ele_et_search,'自动化测试','输入搜索内容-自动化测试')
        self.base.click(ele_btn_search,'搜索按钮')
        self.base.click(ele_host_name,'点击直播间')

    @allure.step('断言直播间观众端界面正常展示')
    def assert_live_room_element(self):
        #断言直播间主播昵称存在
        self.base.assert_element_exist(ele_liveroom_streamer_name)
        #断言直播间主播头像存在
        self.base.assert_element_exist(ele_user_avatar)
        #断言直播间嘉宾席存在
        self.base.assert_element_exist(ele_visitor_avatar)
        #断言直播间粉丝团存在
        self.base.assert_element_exist(ele_live_room_top_fans_tv)
        #断言直播间贡献榜存在
        self.base.assert_element_exist(ele_contribute_tv)
        #断言直播间聊天框存在
        self.base.assert_element_exist(ele_liveroom_im_list)
        #断言直播间发言按钮存在
        self.base.assert_element_exist(ele_liveroom_play_comment)
        #断言直播间连麦按钮存在
        self.base.assert_element_exist(ele_liveroom_play_link_mic)
        #断言直播间分享按钮存在
        self.base.assert_element_exist(ele_liveroom_play_share)
        #断言直播间消息按钮存在
        self.base.assert_element_exist(ele_liveroom_play_private_chat)
        #断言直播间更多按钮存在
        self.base.assert_element_exist(ele_liveroom_play_fun_more)
        #断言直播间礼物按钮存在
        self.base.assert_element_exist(ele_liveroom_play_gift)
        #断言直播间关闭按钮存在
        self.base.assert_element_exist(ele_av_room_top_close)

    @allure.step('点击主播头像')
    def click_ele_user_avatar(self):
        self.base.click(ele_user_avatar,'主播头像')

    @allure.step('断言主播信息卡片界面元素')
    def assert_host_layout_bg(self):
        #断言主播信息卡片主播头像存在
        self.base.assert_element_exist(ele_hostcard_user_avatar)
        #断言主播信息卡片主播昵称存在
        self.base.assert_element_exist(ele_hostcard_nickname)
        #断言主播信息卡片小象号存在
        self.base.assert_element_exist(ele_hostcard_uid)
        #断言主播信息卡片更多按钮存在
        self.base.assert_element_exist(ele_hostcard_more)
        #断言主播信息卡片举报按钮存在
        self.base.assert_element_exist(ele_hostcard_report)
        #断言主播信息卡片用户等级存在
        self.base.assert_element_exist(ele_hostcard_level)
        #断言主播信息卡片个人签名存在
        self.base.assert_element_exist(ele_hostcard_sign)
        #断言主播信息卡片粉丝数存在
        self.base.assert_element_exist(ele_hostcard_fans)
        #断言主播信息卡片关注数存在
        self.base.assert_element_exist(ele_hostcard_follower)
        #断言主播信息卡片送出数存在
        self.base.assert_element_exist(ele_hostcard_send)
        #断言主播信息卡片收到数存在
        self.base.assert_element_exist(ele_hostcard_get)
        #断言主播信息卡片主页按钮存在
        self.base.assert_element_exist(ele_hostcard_homepage)
        #断言主播信息卡片@按钮存在
        self.base.assert_element_exist(ele_hostcard_eit)
        #断言主播信息卡片关注存在
        self.base.assert_element_exist(ele_hostcard_focus)
        #断言主播信息卡片好友存在
        self.base.assert_element_exist(ele_hostcard_friend_status)

    @allure.step('点击进入主播的主页')
    def click_hostcard_homepage(self):
        self.base.click(ele_hostcard_homepage,'主页按钮')
