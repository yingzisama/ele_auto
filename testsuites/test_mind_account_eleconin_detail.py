# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("我的账户-小象币明细")
@allure.feature("我的账户-小象币明细")
class Test_Mind_Account_Eleconin_Detail:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("初始化我的账户模块")
        self.base = self.mind.base
        yield self.mind
        logger.info("结束我的账户模块")

    @allure.story('我的账户-小象币明细')
    @allure.title("我的账户-小象币明细")
    def test_mind_account_eleconin_detail(self, init_live):
        #进入我的账户页面
        init_live.mind_account_tab()
        #进入小象币，点击明细页
        init_live.mind_accout_elecoin()
        init_live.click_mind_account_tv_bar_right()
        #断言余额明细，收入tab，支出tab存在
        init_live.assert_account_eleconin_detail()
