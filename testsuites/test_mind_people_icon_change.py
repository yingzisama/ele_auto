# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("个人中心-换头像")
@allure.feature("个人中心-换头像")
class Test_Mind_People_Center_Icon:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.mind.base
        yield self.mind
        logger.info("结束直播准备模块")

    @allure.story('个人头像更换')
    @allure.title("个人头像更换")
    def test_mind_people_icon_change(self, init_live):
        #进个人资料页
        init_live.click_people_data()
        #截屏当前用户头像
        init_live.save_element_pic('people_icon')
        #拍照，保存头像
        init_live.change_people_icon()
        #断言拍照之前在当前页面不存在
        self.base.assert_not_image_findit('./aseert_pic/people_icon.jpg')
