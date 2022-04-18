# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("个人中心-信息检查")
@allure.feature("个人中心-信息检查")
class Test_Mind_Personal_Check:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("初始化信息检查")
        self.base = self.mind.base
        yield self.mind
        logger.info("结束信息检查")

    @allure.story('个人信息检查')
    @allure.title("个人信息检查")
    def test_mind_personal_check(self, init_live):
        #进mind页
        init_live.click_mind_button()
        #断言用户头像、昵称、小象号、等级勋章、国家、职业、关注数和粉丝数元素存在
        self.base.assert_image_findit('./aseert_pic/mind_person_name.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_ele_userId.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_countries.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_Focus_on.jpg')
        self.base.assert_image_findit('./aseert_pic/mind_fans.jpg')
        #点击关注数
        self.base.click_descriptionContain('关注','关注')
        #断言关注列表数据展示正常
        self.base.assert_element_exist('com.yiwuzhibo:id/tv_bar_title')
        #返回
        self.base.back()
        #点击粉丝
        self.base.click_descriptionContain('粉丝','粉丝')
        #断言粉丝列表数据展示正常
        self.base.assert_element_exist('com.yiwuzhibo:id/tv_bar_title')
