# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#直播按钮
iv_create = 'com.yiwuzhibo:id/iv_create' 

#普通直播
tiv_live = 'com.yiwuzhibo:id/tiv_live'
#OBS直播
tiv_obs_live = 'com.yiwuzhibo:id/tiv_obs_live'

#开播封面
av_preview_cover_bg = 'com.yiwuzhibo:id/av_preview_cover_bg'
#直播标题
av_preview_edit_room_title = 'com.yiwuzhibo:id/av_preview_edit_room_title'
#微信分享
preview_share_wx_friend = 'com.yiwuzhibo:id/preview_share_wx_friend'
#朋友圈分享
preview_share_wx_circle = 'com.yiwuzhibo:id/preview_share_wx_circle'
#facebook分享
preview_share_facebook = 'com.yiwuzhibo:id/preview_share_facebook'
#推特分享
preview_share_twitter = 'com.yiwuzhibo:id/preview_share_twitter'
#line分享
preview_share_line = 'com.yiwuzhibo:id/preview_share_line'

#镜头翻转
preview_switch_camera_tv = 'com.yiwuzhibo:id/preview_switch_camera_tv'
#美颜按钮
preview_filter_tv = 'com.yiwuzhibo:id/preview_filter_tv'
#开始直播
preview_start = 'com.yiwuzhibo:id/preview_start'

#添加封面
cover_add = 'com.yiwuzhibo:id/cover_add'
#相册
photo_album = '//*[@text="相册"]'
#相机栏
camera_photo = '相机'
#第一张图片
first_pic_camera = '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]'
#选择照片-确认
pic_select_confirm = 'com.hihonor.photos:id/head_select_right'
#使用
select_pic_use = 'com.yiwuzhibo:id/activity_crop_photo_confirm'
#审核中
cover_status_tv = '审核中'
#封面删除
cover_delete_click = 'com.yiwuzhibo:id/cover_delete_click'
#删除确认
tv_comfirm = "确定"

#美颜tab
cb_color = 'com.yiwuzhibo:id/cb_color'
#磨皮
buffing_live = '磨皮'
#美白
whitening_live = '美白'
#红润
ruddy_live = '红润'
#状态条
sb_shape_default = 'com.yiwuzhibo:id/sb_shape_default'
#状态值
sb_progress_tv = 'com.yiwuzhibo:id/sb_progress_tv'

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

#滤镜tab
cb_filter = 'com.yiwuzhibo:id/cb_filter'
#原图
rv_filter_01 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'
#缤纷
rv_filter_02 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]'
#蓝调
rv_filter_03 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]'
#柔光
rv_filter_04 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[4]/android.widget.FrameLayout[1]'
#日系
rv_filter_05 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[5]/android.widget.FrameLayout[1]'
#怀旧
rv_filter_06 = '//*[@resource-id="com.yiwuzhibo:id/rv_filter"]/android.widget.LinearLayout[6]/android.widget.FrameLayout[1]'


class Live(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    #进入直播准备阶段
    @allure.step("进入直播准备阶段")
    def start_live_prepare(self):
        self.base.click(iv_create,iv_create)
        self.base.wait_element_appear(tiv_live,tiv_live,1)
        self.base.click(tiv_live,tiv_live)

    @allure.step("创建直播间")
    def start_live(self):
        self.base.click(iv_create,iv_create)
        self.base.wait_element_appear(tiv_live,tiv_live,1)
        self.base.click(tiv_live,tiv_live)
        self.base.click(preview_start,preview_start)
        self.base.wait_time()
        self.base.assert_exist('粉丝团')

    @allure.step("设置直播间标题")
    def start_live_set_title(self,titleName):
        self.base.send_keys(av_preview_edit_room_title,titleName,av_preview_edit_room_title)
        self.base.back()

    @allure.step("启动直播")
    def start_live_true(self):
        self.base.click(preview_start,preview_start)

    @allure.step("选择封面")
    def choose_cover(self):
        self.base.click(av_preview_cover_bg,av_preview_cover_bg)
        self.base.click(cover_add,cover_add)

    @allure.step("添加相册第一张")
    def add_first_camera(self):
        self.base.click(photo_album,photo_album)
        self.base.click(camera_photo,camera_photo)
        self.base.click(first_pic_camera,first_pic_camera)
        self.base.click(pic_select_confirm,pic_select_confirm)
        self.base.click(select_pic_use,select_pic_use)

    @allure.step("删除当前直播封面图片")
    def cover_delete(self):
        self.base.click(cover_delete_click,cover_delete_click)
        self.base.click(tv_comfirm,tv_comfirm)

    @allure.step("微信分享")
    def live_share_wx(self):
        self.base.click(preview_share_wx_friend,preview_share_wx_friend)

    @allure.step("朋友圈分享")
    def live_share_wx_circle(self):
        self.base.click(preview_share_wx_circle,preview_share_wx_circle)

    @allure.step("facebook分享")
    def live_share_facebook(self):
        self.base.click(preview_share_facebook,preview_share_facebook)

    @allure.step("twitter分享")
    def live_share_twitter(self):
        self.base.click(preview_share_twitter,preview_share_twitter)

    @allure.step("line分享")
    def live_share_line(self):
        self.base.click(preview_share_line,preview_share_line)

    @allure.step('打开美颜设置')
    def live_beauty_face_tools(self):
        self.base.click(preview_filter_tv,preview_filter_tv)

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

    @allure.step('点击磨皮')
    def live_click_buffing(self):
        self.base.click(buffing_live,buffing_live)

    @allure.step('点击美白')
    def live_click_whitening(self):
        self.base.click(whitening_live,whitening_live)

    @allure.step('点击红润')
    def live_click_ruddy(self):
        self.base.click(ruddy_live,ruddy_live)

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

    @allure.step('滑动进度条')
    def live_assert_swipe_value(self):
        self.live_swipe_shape_left()
        self.live_get_swipe_value_0()
        self.live_swipe_shape_right()
        self.live_get_swipe_value_100()
