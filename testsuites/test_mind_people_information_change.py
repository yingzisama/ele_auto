# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("个人中心-设置个人信息")
@allure.feature("个人中心-设置个人信息")
class Test_Mind_People_Information_Change:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("初始化修改个人信息结束")
        self.base = self.mind.base
        yield self.mind
        logger.info("修改个人信息结束")

    @allure.story('个人资料-信息修改')
    @allure.title("个人资料-信息修改")
    def test_mind_people_information_change(self, init_live):
        #进个人资料页
        init_live.click_people_data()
        #修改昵称（正在自动化测试——公会主播）
        init_live.change_mind_nickname('公会主播')
        #修改性别（不公开——男）
        init_live.change_mind_sex('男')
        #修改国家/地区（爱尔兰——阿曼）
        init_live.change_mind_countries_aman()
        #修改城市（北京——上海）
        init_live.change_mind_city('上海')
        #修改生日
        init_live.change_mind_birthday()
        #修改职业（新职业——主播）
        init_live.change_mind_professional('主播')
        #上滑，查看下面
        self.base.back()
        self.base.wait_time()
        self.base.swipe_up()
        #修改个性签名（没有个性签名——没有个性签名2）
        init_live.change_mind_signature('没有个性签名2')
        #退回到mind页
        init_live.editor_information_done()
        self.base.back()
        #断言修改生效（昵称修改成功，出现性别icon，出现国家，出现星座，出现职业）
        init_live.assert_host_information_change_success()
        #还原修改
        init_live.reduction_mind_information('正在自动化测试')
        #完成修改
        init_live.editor_information_done()
