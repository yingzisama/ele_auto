# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.mind import Mind
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("我的账户-小象币充值")
@allure.feature("我的账户-小象币充值")
class Test_Mind_Account:
    @pytest.fixture
    def init_live(self):
        self.mind = Mind(self.driver)
        logger.info("初始化我的账户模块")
        self.base = self.mind.base
        yield self.mind
        logger.info("结束我的账户模块")

    @allure.story('我的账户-小象币充值')
    @allure.title("我的账户-小象币充值")
    def test_mind_account(self, init_live):
        #进入我的账户页面
        init_live.mind_account_tab()
        #断言相关元素存在
        init_live.assert_mind_account_element_exits()
        #进入小象币充值页
        init_live.click_ele_conin_bk()
        #断言充值页面元素存在
        init_live.assert_ele_conin_page()
        #选择第一个充值档位，进入充值页
        init_live.click_mind_account_gear_01()
        #断言充值页元素正常
        init_live.assert_account_gear_page()
