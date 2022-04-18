# coding:gbk
import pytest
from tools.loggers import JFMlogging
import allure
from module.live import Live
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间封面添加删除")
@allure.feature("直播间封面添加删除")
class Test_Live_cover:
    @pytest.fixture
    def init_live(self):
        self.live = Live(self.driver)
        logger.info("初始化直播准备模块")
        self.base = self.live.base
        yield self.live
        logger.info("结束直播准备模块")

    @allure.story('直播间封面添加删除')
    @allure.title("封面添加/删除")
    def test_add_cover(self, init_live):
        init_live.start_live_prepare()
        init_live.choose_cover()
        self.base.assert_exist('相册')
        init_live.add_first_camera()
        self.base.assert_exist('审核中')
        init_live.cover_delete()
        self.base.assert_not_exist('审核中')
