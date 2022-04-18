# coding:gbk
from tools.loggers import JFMlogging
from module.base import Base
import allure
logger = JFMlogging().getloger()

#mind页
mind_downbutton = '//*[@resource-id="com.yiwuzhibo:id/tab_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]'
#签到按钮
mind_sign_in = '//android.widget.ScrollView/android.widget.ImageView[1]'
#头像框
mind_man_icon = '//android.widget.ScrollView/android.widget.ImageView[2]'

#个人中心
mind_people_center = '个人中心'
#个人资料
mind_people_data = '个人资料'
#用户头像
mind_people_icon_editor = '编辑'
#相册
mind_people_photograph = '拍照'
#拍照button
mind_photograph_button = 'com.huawei.camera:id/place_holder_shutter_button'
#拍照保存
mind_photograph_done = 'com.huawei.camera:id/done_button'
#确认替换照片
mind_menu_crop = 'com.yiwuzhibo:id/menu_crop'
#编辑完成
mind_editor_done = '完成'

#我的账户
mind_my_account = '我的账户'
#主播中心
mind_host_center = '主播中心'
#我的等级
mind_my_level = '我的等级'
#我的装扮
mind_my_dress = '我的装扮'
#小象商场
mind_ele_mall = '小象商城'
#我的视频
mind_my_video = '我的视频'
#昵称框
mind_my_nickname_editor = '正在自动化测试, 请填写'
#性别栏
mind_sex = '性别'
#性别-男
mind_sex_man = '男'
#性别-女
mind_sex_woman = '女'
#性别-不公开
mind_sex_unkown = '不公开'
#国家/地区
mind_countries = "国家/地区"
#国家-爱尔兰
mind_countries_Irish = '爱尔兰'
#国家-阿曼
mind_countries_aman = '阿曼'
#城市
mind_city_editor = '//android.widget.ScrollView/android.widget.EditText[2]'
#生日
mind_birthday_editor = '生日'
#确定
mind_birthday_determine = '确定'
#职业
mind_professional_editor = '新职业, 请填写'
#个性签名
mind_signature_editor = '没有个性签名, 创作一个引人注目的签名吧~'
#个性签名-mes
mind_signature_editor_mes = '没有个性签名'
#还原个性签名
reduction_mind_signature_editor = '没有个性签名2, 创作一个引人注目的签名吧~'
#修改后的昵称
mind_change_nickname = '公会主播, 请填写'
#还原职业
reduction_mind_professional_editor = '主播, 请填写'
#我的账户title
mind_tv_bar_title = 'com.yiwuzhibo:id/tv_bar_title'
#小象币
mind_ele_coin = '小象币'
#象豆
mind_ele_bean = '象豆'
#小象币卡片
mind_ele_conin_bk = 'com.yiwuzhibo:id/ele_coin_bk'
#小象币icon
mind_elecoin_icon = 'com.yiwuzhibo:id/elecoin_icon'
#小象币金额
mind_ele_coin_count = 'com.yiwuzhibo:id/ele_coin_count'
#小象币充值按钮
mind_elecoin_recharge = 'com.yiwuzhibo:id/elecoin_recharge'
#象豆卡片
mind_ele_bean_bk = 'com.yiwuzhibo:id/ele_bean_bk'
#象豆icon
mind_elebean_icon = 'com.yiwuzhibo:id/elebean_icon'
#象豆余额
mind_ele_bean_count = 'com.yiwuzhibo:id/ele_bean_count'
#象豆礼包tab
mind_elebean_packet = 'com.yiwuzhibo:id/elebean_packet'
#象豆明细tab
mind_elebean_detail = 'com.yiwuzhibo:id/elebean_detail'
#象豆礼包title
mind_bean_gift_page_title = '象豆礼包'
#象豆明细title
mind_bean_gift_page_detail = '象豆明细'
#充值小象币title
mind_account_tv_bar_title = "com.yiwuzhibo:id/tv_bar_title"
#用户头像
mind_account_my_head="com.yiwuzhibo:id/my_head"
#用户昵称
mind_account_nick_name="com.yiwuzhibo:id/nick_name"
#小象币icon
mind_account_my_elecoin_icon="com.yiwuzhibo:id/my_elecoin_icon"
#小象币余额
mind_account_my_elebean_title="com.yiwuzhibo:id/my_elebean_title"
#用户实际小象币余额
mind_account_tv_balance="com.yiwuzhibo:id/tv_balance"
#查询明细
mind_account_tv_bar_right="com.yiwuzhibo:id/tv_bar_right"
#充值档位-1
mind_account_gear_01='//*[@resource-id="com.yiwuzhibo:id/rv_recharge"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
#支付方式
mind_pay_type = 'com.yiwuzhibo:id/tv_item_pay_type'
#支付按钮
mind_bgv_pay = 'com.yiwuzhibo:id/bgv_pay'
#充值数额
mind_pay_amount = 'com.yiwuzhibo:id/tv_pay_amount'
#余额明细title
mind_detail_page_title = '余额明细'
#收入明细tab
mind_income_detail_tab = '收入第 1 个标签，共 2 个'
#支出明细tab
mind_spending_detail_tab = '支出第 2 个标签，共 2 个'
#主播中心-我的收益
mind_host_center_earnings = '我的收益'
#提现记录
mind_host_center_earnings_withdrawal_record = '提现记录'
#主播中心-我的收益
mind_host_center_everytoday_earnings = '每日收益'
#主播中心-我的收益
mind_host_center_today_income = '今日收入'
#主播中心-我的收益
mind_host_center_month_income = '本月收入'
#主播中心-我的收益
mind_host_center_all_income = '总计收入'
#每日收益
#主播中心-签约公会
mind_host_center_signing = '签约公会'
#主播中心-直播记录
mind_host_center_record = '直播记录'
#主播中心-贡献榜
mind_host_center_contribution = '贡献榜'
#主播中心-粉丝团
mind_host_center_fans = '粉丝团'
#主播中心-我的成就
mind_host_center_achievement = '我的成就'
#主播中心-直播间管理员
mind_host_center_administrator = '直播间管理员'
#主播中心-封禁管理
mind_host_center_banned = '封禁管理'


class Mind(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("点击进入mind页")
    def click_mind_button(self):
        self.base.click(mind_downbutton,mind_downbutton)

    @allure.step("进入个人中心")
    def click_people_center(self):
        self.base.click(mind_downbutton,mind_downbutton)
        self.base.click_description(mind_people_center,mind_people_center)

    @allure.step('进个人资料页')
    def click_people_data(self):
        self.base.click(mind_downbutton,mind_downbutton)
        self.base.click_description(mind_people_center,mind_people_center)
        self.base.click_description(mind_people_data,mind_people_data)

    @allure.step('替换用户头像')
    def change_people_icon(self):
        self.base.click_description(mind_people_icon_editor,mind_people_icon_editor)
        self.base.click_description(mind_people_photograph,mind_people_photograph)
        self.base.wait_time()
        self.base.click(mind_photograph_button,mind_photograph_button)
        self.base.click(mind_photograph_done,mind_photograph_done)
        self.base.click(mind_menu_crop,mind_menu_crop)
        self.base.wait_time(1)
        self.base.click_description(mind_editor_done,mind_editor_done)

    @allure.step('保存用户头像图片')
    def save_element_pic(self,pic):
        self.base.wait_time(1)
        self.base.save_element_screenshot_description(r'D:\workspace_new\uiauto2_ele\aseert_pic\people_icon.jpg',mind_people_icon_editor,pic)

    @allure.step('修改昵称')
    def change_mind_nickname(self,nickname):
        self.base.set_text_contanis(mind_my_nickname_editor,nickname,mind_my_nickname_editor)
        self.base.back()

    @allure.step('修改性别')
    def change_mind_sex(self,sex):
        self.base.click_description_center(mind_sex)
        self.base.wait_time(1)
        if sex == '男':
            self.base.click_description(mind_sex_man,mind_sex_man)
        elif sex == '女':
            self.base.click_description(mind_sex_woman,mind_sex_man)
        else:
            self.base.click_description(mind_sex_unkown,mind_sex_man)

    @allure.step('修改国家/地区-爱尔兰')
    def change_mind_countries(self):
        self.base.click_description_center(mind_countries)
        self.base.wait_time()
        self.base.click_description(mind_countries_Irish,mind_countries_Irish)

    @allure.step('修改国家/地区-阿曼')
    def change_mind_countries_aman(self):
        self.base.click_description_center(mind_countries)
        self.base.wait_time()
        self.base.click_description(mind_countries_aman,mind_countries_aman)

    @allure.step('修改城市')
    def change_mind_city(self,newCity):
        self.base.click(mind_city_editor,mind_city_editor)
        self.base.send_keys(mind_city_editor,newCity,mind_city_editor)
        self.base.back()

    @allure.step('修改生日')
    def change_mind_birthday(self):
        self.base.click_description(mind_birthday_editor,mind_birthday_editor)
        self.base.click_description(mind_birthday_determine,mind_birthday_determine)

    @allure.step('职业')
    def change_mind_professional(self,setProfessional):
        self.base.click(mind_professional_editor,mind_professional_editor)
        self.base.set_text_FastInputIME(setProfessional,setProfessional)

    @allure.step('个性签名')
    def change_mind_signature(self,new_signature):
        self.base.click(mind_signature_editor,mind_signature_editor)
        self.base.set_text_FastInputIME(new_signature,new_signature)

    @allure.step('完成修改')
    def editor_information_done(self):
        self.wait_time()
        self.base.click_description(mind_editor_done,mind_editor_done)

    @allure.step('断言用户信息修改成功')
    def assert_host_information_change_success(self):
        self.base.assert_image_findit('./aseert_pic/change_people_countries.jpg')
        self.base.assert_image_findit('./aseert_pic/change_people_nickname.jpg')
        self.base.assert_image_findit('./aseert_pic/change_people_professional.jpg')
        self.base.assert_image_findit('./aseert_pic/change_people_sex.jpg')

    @allure.step('还原个人资料')
    def reduction_mind_information(self,reduction_nickname):
        self.base.click_description(mind_people_center,mind_people_center)
        self.base.click_description(mind_people_data,mind_people_data)
        self.base.click(mind_change_nickname,mind_change_nickname)
        self.base.set_text_FastInputIME(reduction_nickname,reduction_nickname)
        self.change_mind_sex('不公开')
        self.change_mind_countries()
        self.base.click(reduction_mind_professional_editor,reduction_mind_professional_editor)
        self.base.set_text_FastInputIME('新职业','新职业')
        self.base.back()
        self.base.wait_time()
        self.base.swipe_up()
        self.base.click(reduction_mind_signature_editor,reduction_mind_signature_editor)
        self.base.set_text_FastInputIME(mind_signature_editor_mes,mind_signature_editor_mes)

    @allure.step('进入我的账户')
    def mind_account_tab(self):
        self.click_mind_button()
        self.base.click_description('我的账户','我的账户')

    @allure.step('点击我的小象币')
    def mind_accout_elecoin(self):
        self.base.click(mind_ele_conin_bk,'小象币卡片')

    @allure.step('点击象豆卡片')
    def mind_accout_elebean(self):
        self.base.click(mind_ele_bean_bk,'点击象豆卡片')

    @allure.step('断言我的账户相关元素存在')
    def assert_mind_account_element_exits(self):
        self.base.assert_element_exist(mind_tv_bar_title)
        self.base.assert_exist(mind_ele_coin)
        self.base.assert_exist(mind_ele_bean)
        self.base.assert_element_exist(mind_ele_coin_count)
        self.base.assert_element_exist(mind_ele_bean_count)
        self.base.assert_element_exist(mind_elecoin_recharge)

    @allure.step('点击小象币卡片')
    def click_ele_conin_bk(self):
        self.base.click(mind_ele_conin_bk,'小象币充值卡片')

    @allure.step('点击象豆卡片')
    def click_ele_bean_bk(self):
        self.base.click(mind_ele_conin_bk,'象豆卡片')

    @allure.step('断言小象币充值页面')
    def assert_ele_conin_page(self):
        self.base.assert_element_exist(mind_account_tv_bar_title)
        self.base.assert_element_exist(mind_account_my_head)
        self.base.assert_element_exist(mind_account_nick_name)
        self.base.assert_element_exist(mind_account_my_elecoin_icon)
        self.base.assert_element_exist(mind_account_my_elebean_title)
        self.base.assert_element_exist(mind_account_tv_balance)
        self.base.assert_element_exist(mind_account_tv_bar_right)

    @allure.step('点击小象币充值档位1')
    def click_mind_account_gear_01(self):
        self.base.click(mind_account_gear_01,'充值档位1-60小象币')

    @allure.step('断言充值页面')
    def assert_account_gear_page(self):
        self.base.assert_element_exist(mind_pay_type)
        self.base.assert_element_exist(mind_bgv_pay)
        self.base.assert_element_exist(mind_pay_amount)

    @allure.step('点击查询明细')
    def click_mind_account_tv_bar_right(self):
        self.base.click(mind_account_tv_bar_right,'查询明细')

    @allure.step('断言小象币余额明细界面展示正常')
    def assert_account_eleconin_detail(self):
        self.base.assert_element_description_exist(mind_detail_page_title)
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_income.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_spending.jpg')

    @allure.step('点击象豆礼包tab')
    def click_mind_elebean_packet(self):
        self.base.click(mind_elebean_packet,'象豆礼包tab')

    @allure.step('点击象豆明细tab')
    def click_mind_elebean_detail(self):
        self.base.click(mind_elebean_detail,'象豆明细tab')

    @allure.step('断言象豆礼包')
    def assert_mind_bean_gift_page(self):
        self.base.assert_element_description_exist(mind_bean_gift_page_title)
        self.base.assert_image_findit('./aseert_pic/mind_account_bean_gift_received.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_account_bean_gift_Sendout.jpg')

    @allure.step('断言象豆礼包')
    def assert_mind_bean_detail_page(self):
        self.base.assert_element_description_exist(mind_bean_gift_page_detail)
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_income.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_account_detail_spending.jpg')

    @allure.step('进入主播中心')
    def click_mind_host_center(self):
        self.click_mind_button()
        self.base.click_description(mind_host_center,mind_host_center)

    @allure.step('进入主播中心-我的收益')
    def click_mind_host_center_my_earnings(self):
        self.click_mind_host_center()
        self.base.click_description(mind_host_center_earnings,mind_host_center_earnings)

    @allure.step('断言我的收益页面展示正常')
    def assert_mind_my_earnings(self):
        self.base.assert_element_description_exist(mind_host_center_earnings_withdrawal_record)
        self.base.assert_element_description_exist(mind_host_center_earnings)
        self.base.assert_element_description_exist(mind_host_center_today_income)
        self.base.assert_element_description_exist(mind_host_center_month_income)
        self.base.assert_element_description_exist(mind_host_center_all_income)
