# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#搜索按钮
ele_iv_search = 'com.yiwuzhibo:id/icon_fun1'
#搜索框
ele_et_search = 'com.yiwuzhibo:id/et_search'
#主播名字
ele_host_name = 'com.yiwuzhibo:id/iv_avatar'
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
# 礼物按钮
ele_liveroom_gift_button = 'com.yiwuzhibo:id/liveroom_play_gift'
# 榜单(人气榜,魅力榜，PK榜，周星榜)
ele_liveroom_rank_1_content = 'com.yiwuzhibo:id/tv_content'
# 普通小象币礼物
ele_liveroom_common_coin_gift = '啾咪'
# 成长类礼物
ele_liveroom_grow_gift = '玫瑰'
# 成长类礼物-玫瑰花丛
ele_liveroom_grow_gift_bigmeigui = '玫瑰花丛'
# 礼物栏-象豆tab
ele_liveroom_bean_tab = '象豆'
# 礼物栏-小象tab
ele_liveroom_ele_tab = '小象'
# 礼物栏-趣味tab
ele_liveroom_quwei_tab = '趣味'
# 礼物栏-热门tab
ele_liveroom_hot_tab = '热门'
# 礼物栏-特权tab
ele_liveroom_tequan_tab = '特权'
# 普通象豆礼物
ele_liveroom_common_bean_gift = '蛋卷寿司'
# 滤镜礼物
ele_liveroom_filter_gift = '春田花花'
# 游戏礼物
ele_liveroom_game_gift = '金足球'
# 粉丝团礼物
ele_liveroom_fans_gift = '粉丝团'
# 涂鸦礼物
ele_liveroom_graffiti_gift = '比心'
# 涂鸦区域
ele_liveroom_graffiti_center = 'com.yiwuzhibo:id/doddle_view'
# 礼物栏-赠送按钮
ele_liveroom_gift_sent_button = '赠送'
# 礼物栏-批量赠送选择入口
ele_liveroom_gift_sent_batch = 'com.yiwuzhibo:id/gift_send_quantity_iv'
# 礼物栏-批量赠送选择66
ele_liveroom_gift_sent_batch66 = '//*[@resource-id="com.yiwuzhibo:id/count_tv_container"]/android.widget.TextView[5]'
# 礼物栏-combo按钮
ele_liveroom_gift_sent_combo = 'com.yiwuzhibo:id/text_combo'
# 退出按钮
ele_av_room_top_close = 'com.yiwuzhibo:id/av_room_top_close'
# 主播信息卡片-主播头像
ele_hostcard_user_avatar = 'com.yiwuzhibo:id/user_avatar'
# 主播信息卡片-主播昵称
ele_hostcard_nickname = 'com.yiwuzhibo:id/av_room_person_name'
# 主播信息卡片-小象号
ele_hostcard_uid = 'com.yiwuzhibo:id/ll_room_person_uid'
# 主播信息卡片-更多按钮
ele_hostcard_more = 'com.yiwuzhibo:id/av_room_person_manager'
# 主播信息卡片-举报
ele_hostcard_report = 'com.yiwuzhibo:id/av_room_person_report'
# 主播信息卡片-用户等级
ele_hostcard_level = 'com.yiwuzhibo:id/av_room_person_tag'
# 主播信息卡片-个人签名
ele_hostcard_sign = 'com.yiwuzhibo:id/av_room_person_sign'
# 主播信息卡片-粉丝数
ele_hostcard_fans = 'com.yiwuzhibo:id/av_room_person_detail_fans'
# 主播信息卡片-关注数
ele_hostcard_follower = 'com.yiwuzhibo:id/av_room_person_detail_follower'
# 主播信息卡片-送出数
ele_hostcard_send = 'com.yiwuzhibo:id/av_room_person_detail_send'
# 主播信息卡片-收到数
ele_hostcard_get = 'com.yiwuzhibo:id/av_room_person_detail_get'
# 主播信息卡片-主页
ele_hostcard_homepage = 'com.yiwuzhibo:id/av_room_person_detail_main'
# 主播信息卡片-@
ele_hostcard_eit = 'com.yiwuzhibo:id/av_room_person_detail_at'
# 主播信息卡片-关注
ele_hostcard_focus = 'com.yiwuzhibo:id/av_room_person_detail_focus'
# 主播信息卡片-好友
ele_hostcard_friend_status = 'com.yiwuzhibo:id/av_room_friend_status'
# 主播信息卡片-拉黑
ele_hostcard_shield = '拉黑'
# 拉黑-确定
ele_hostcard_shield_comfirm = 'com.yiwuzhibo:id/tv_comfirm'
# 发言栏-发送
ele_input_confirm_tv = 'com.yiwuzhibo:id/input_confirm_tv'
# Mind页
mind_downbutton = '//*[@resource-id="com.yiwuzhibo:id/tab_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]'
# 个人中心
mind_people_center = '个人中心'
# 黑名单管理
mind_shield_manager = '黑名单管理'

class Audience(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("进入直播间")
    def enter_live_room(self):
        self.base.click(ele_iv_search,'搜索按钮')
        self.base.send_keys(ele_et_search,'12229221','输入搜索内容-12229221')
        self.base.enter()
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

    @allure.step('断言主播主页界面元素')
    def assert_host_person_detail(self):
        #断言主播关注数
        self.base.assert_image_findit('./aseert_pic/audience_detail_follower.jpg')
        #断言主播粉丝数
        self.base.assert_image_findit('./aseert_pic/audience_detail_fans.jpg')
        #断言主播贡献榜入口
        self.base.assert_image_findit('./aseert_pic/audience_detail_contributionRanking.jpg')
        #断言主播粉丝榜入口
        self.base.assert_image_findit('./aseert_pic/audience_detail_fansRanking.jpg')
        #断言主播短视频作品tab
        self.base.assert_image_findit('./aseert_pic/audience_detail_myVideo.jpg')
        #断言主播喜欢的短视频作品tab
        self.base.assert_image_findit('./aseert_pic/audience_detail_myLikeVideo.jpg')
        #断言主播关注按钮
        self.base.assert_image_findit('./aseert_pic/audience_detail_focus.jpg')

    @allure.step('点击@主播')
    def click_hostcard_eit(self):
        self.base.click(ele_hostcard_eit,'@')

    @allure.step('发送')
    def click_input_confirm_tv(self):
        self.base.click(ele_input_confirm_tv,'发送')

    @allure.step('断言发言内容存在')
    def assert_live_room_im(self):
        a = self.base.elements_exist('com.yiwuzhibo:id/live_room_im_tv','a 正在自动化测试：@自动化测试主播端 111')
        assert a == True

    @allure.step('主播信息卡片-获取粉丝数')
    def get_hostcard_fans_num(self):
        fans_str = self.base.get_element_text(ele_hostcard_fans)
        fans = int(fans_str)
        logger.info("当前粉丝数为:{}".format(fans))
        return fans

    @allure.step('主播信息卡片-关注主播')
    def click_hostcard_focus(self):
        self.base.click(ele_hostcard_focus,ele_hostcard_focus)

    @allure.step('主播信息卡片-拉黑主播')
    def click_hostcard_shield(self):
        self.base.click(ele_hostcard_more,'更多')
        self.base.click(ele_hostcard_shield,'拉黑')
        self.base.click(ele_hostcard_shield_comfirm,'确定')

    @allure.step('进入个人中心-黑名单管理')
    def click_mind_shield_manager(self):
        self.base.click(mind_downbutton,'mind页')
        self.base.click_description(mind_people_center,'个人中心')
        self.base.click_description(mind_shield_manager,'黑名单管理')

    @allure.step('断言拉黑主播存在')
    def assert_shield_host_exist(self):
        self.base.assert_image_findit('./aseert_pic/mind_shield_manager.jpg')

    @allure.step('点击移除黑名单用户')
    def click_shield_host_remove(self):
        self.base.click_image_findit('./aseert_pic/mind_shield_manager_remove.jpg')

    @allure.step('退出直播间')
    def click_ele_av_room_top_close(self):
        self.base.click(ele_av_room_top_close,'离开直播间')

    @allure.step('主播信息卡片-点击举报')
    def click_ele_hostcard_report(self):
        self.base.click(ele_hostcard_report,'举报')

    @allure.step('输入举报内容')
    def input_report_content(self,message):
        self.base.click('详细描述举报理由...','点击内容')
        self.base.set_text_FastInputIME(message,message)
        self.base.back()

    @allure.step('点击提交')
    def click_report_submit(self):
        self.base.click_description('提交','提交')

    @allure.step('断言举报成功')
    def assert_report_success(self):
        self.base.assert_get_toast_message('举报成功，平台将会在24小时之内给出回复')

    @allure.step('点击观众头像')
    def click_myself_icon(self):
        self.base.click(ele_visitor_avatar,'观众席自己头像')

    @allure.step('点击打开礼物面板')
    def live_click_gift_button(self):
        self.base.click(ele_liveroom_gift_button,'打开礼物面板')

    @allure.step('赠送小象币礼物-啾咪')
    def live_click_10coin_gift(self):
        self.base.click(ele_liveroom_common_coin_gift,'点击礼物-啾咪')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送象豆礼物-蛋卷寿司')
    def live_click_20bean_gift(self):
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_common_bean_gift,'点击礼物-蛋卷寿司')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送成长礼物-玫瑰')
    def live_click_2coin_grow_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.click(ele_liveroom_grow_gift,'点击成长礼物-玫瑰')
        self.base.wait_time(1)
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送成长礼物-玫瑰100次')
    def live_click_100_grow_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.click(ele_liveroom_grow_gift,'点击成长礼物-玫瑰')
        self.base.wait_time(1)
        self.base.click_more(ele_liveroom_gift_sent_button,100,'点击赠送')

    @allure.step('断言-玫瑰花丛(解锁)存在')
    def assert_big_meigui(self):
        self.base.assert_image_findit('./aseert_pic/big_meigui.jpg')

    @allure.step('赠送成长礼物-玫瑰花丛')
    def live_click_grow_gift_bigmeigui(self):
        self.base.click(ele_liveroom_grow_gift_bigmeigui,'点击成长礼物-玫瑰花丛')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送滤镜礼物-春田花花')
    def live_click_filter_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.swipe_x1y1x2y2(0.827, 0.806,0.121,  0.806)
        self.base.swipe_x1y1x2y2(0.827, 0.806,0.121,  0.806)
        self.base.click(ele_liveroom_filter_gift,'点击滤镜礼物-春田花花')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送游戏礼物-金足球')
    def live_click_game_gift(self):
        self.base.click(ele_liveroom_hot_tab,'点击切换到礼物-热门tab')
        self.base.click(ele_liveroom_game_gift,'点击游戏礼物-金足球')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送粉丝团礼物-粉丝团')
    def live_click_fans_gift(self):
        self.base.click(ele_liveroom_tequan_tab,'点击切换到礼物-特权tab')
        self.base.click(ele_liveroom_fans_gift,'点击游戏礼物-粉丝团')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('赠送小象币礼物combo-啾咪')
    def live_click_10coin_gift_combo(self):
        self.base.click(ele_liveroom_common_coin_gift,'点击礼物-啾咪')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')
        self.base.click(ele_liveroom_gift_sent_combo,'点击combo赠送')

    @allure.step('赠送象豆礼物combo-蛋卷寿司')
    def live_click_20bean_gift_combo(self):
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_common_bean_gift,'点击礼物-蛋卷寿司')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')
        self.base.click(ele_liveroom_gift_sent_combo,'点击combo赠送')

    @allure.step('赠送涂鸦礼物-比心')
    def live_click_graffiti_gift(self):
        self.base.click(ele_liveroom_ele_tab,'点击礼物栏-小象tab')
        self.base.click(ele_liveroom_graffiti_gift,'点击礼物-比心')
        self.base.click_more(ele_liveroom_graffiti_center,10,'点击涂鸦区域10次')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('断言礼物栏-余额')
    def assert_gift_balance(self,num):
        self.base.assert_exist(num)

    @allure.step('断言-评论区出现送礼消息')
    def assert_gift_message(self):
        self.base.assert_image_findit('./aseert_pic/send_gift.png')

    @allure.step('批量送礼-啾咪')
    def live_click_10coin_gift_batch66(self):
        self.base.click(ele_liveroom_common_coin_gift,'点击礼物-啾咪')
        self.base.click(ele_liveroom_gift_sent_batch,'点出批量选择')
        self.base.click(ele_liveroom_gift_sent_batch66,'选择批量数66')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')

    @allure.step('批量赠送象豆礼物-蛋卷寿司')
    def live_click_20bean_gift_batch66(self):
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_common_bean_gift,'点击礼物-蛋卷寿司')
        self.base.click(ele_liveroom_gift_sent_batch,'点出批量选择')
        self.base.click(ele_liveroom_gift_sent_batch66,'选择批量数66')
        self.base.click(ele_liveroom_gift_sent_button,'点击赠送')