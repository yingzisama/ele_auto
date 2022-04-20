# coding:gbk
import re, time
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


class Base(object):

    def __init__(self, driver):
        self.d = driver
        self.width = self.get_window_size()[0]
        self.height = self.get_window_size()[1]

    def click(self, element, log_text):
        """
        元素点击
        element:元素名称
        log_text:打印log的文案
        xpath使用方法
        1.包含
        d.xpath(u"//android.widget.TextView[contains(@text,'购买 ?0?6')]").click()
        2.全匹配
        d.xpath(u"//android.widget.TextView[@text='购买 ?0?64.99']").click()
        3.匹配开始字符
        d.xpath(u"//android.widget.TextView[starts-with(@text,'购买 ?0?6')]").click()
        :return:
        """
        if str(element).startswith("com"):
            self.d(resourceId=element).click()
        elif re.findall("//", str(element)):
            self.d.xpath(element).click()
        else:
            self.d(text=element).click()
        logger.info("点击元素:「{}」".format(log_text))

    def click_text_contains(self,element,log_text):
        """
        部分text元素点击
        element:元素名称
        log_text:打印log的文案
        """
        self.d(textContains=element).click()
        logger.info("点击元素:「{}」".format(log_text))

    def click_description(self, element, log_text):
        """
        description元素点击
        element:元素名称
        log_text:打印log的文案
        """
        self.d(description=element).click()
        logger.info("点击元素:「{}」".format(log_text))

    def click_descriptionContain(self, element, log_text):
        """
        description元素点击
        element:元素名称
        log_text:打印log的文案
        """
        self.d(descriptionContains=element).click()
        logger.info("点击元素:「{}」".format(log_text))

    def click_description_center(self, element):
        """
        点击description控件中间
        :param element:
        :return:
        """
        x,y = self.d(description=element).center()
        self.d.click(x,y)
        logger.info("点击元素「{}」".format(element))

    def send_keys(self, element, sendtext, log_text):
        """
        文本输入
        element:元素名称
        sendtext:输入的文案
        log_text:打印log的文案
        :return:
        """
        if str(element).startswith("com"):
            self.d(resourceId=element).set_text(sendtext)
        elif re.findall("//", str(element)):
            self.d.xpath(element).set_text(sendtext)
        else:
            self.d(text=element).set_text(sendtext)

        logger.info("输入文字「{}」".format(log_text))

    def set_text_contanis(self, element, sendtext, log_text):
        """
        文本输入
        element:元素名称
        sendtext:输入的文案
        log_text:打印log的文案
        :return:
        """
        text_all = self.d(textContains=element).get_text()
        self.d(text=text_all).click()
        self.d.send_keys(sendtext,clear=True)

        logger.info("输入文字「{}」".format(log_text))

    def set_text_FastInputIME(self, sendtext, log_text):
        """
        文本输入
        sendtext:输入的文案
        log_text:打印log的文案
        :return:
        """
        self.d.send_keys(sendtext,clear=True)
        logger.info("输入文字「{}」".format(log_text))

    def double_click(self, x, y, time=0.5):
        """
        双击
        :return:
        """
        self.d.double_click(x, y, time)
        logger.info("点击坐标:「{}」,「{}」".format(x, y))

    def get_window_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        window_size = self.d.window_size()
        width = int(window_size[0])
        height = int(window_size[1])
        return width, height

    def swipe_up(self, duration=0.5):
        """
        向上滑动,查看下面的内容
        :return:
        """
        self.d.swipe_ext("up",scale=duration)
        logger.info("向下滑动，查看下面的内容")

    def swipe_down(self, duration=0.5):
        """
        向下滑动，查看上面的内容
        :return:
        """
        self.d.swipe_ext("down",scale=duration)
        logger.info("向下滑动，查看上面的内容")

    def swipe_left(self, duration=0.5):
        """
        向左滑动，查看右面的内容
        :return:
        """
        self.d.swipe_ext("down",scale=duration)
        logger.info("向左滑动，查看右面的内容")

    def swipe_right(self, duration=0.5):
        """
        向右滑动，查看左面的内容
        :return:
        """
        self.d.swipe_ext("down",scale=duration)
        logger.info("向右滑动，查看左面的内容")

    def swipe_x1y1x2y2(self, x1, y1, x2,y2):
        """
        坐标值滑动
        """
        self.d.swipe(x1,y1,x2,y2)
        logger.info("拖动元素「{}」「{}」至元素「{}」「{}」处".format(x1,y1,x2,y2))

    def swipe_to_element(self, element1, element2, duration=0.25):
        """
        滑动到某个元素
        :param element1: 起始元素
        :param element2: 目标元素
        :param duration: 滑动时间
        :return:
        """
        self.d(text=element1).drag_to(text=element2, duration=duration)
        logger.info("拖动元素「{}」至元素「{}」处".format(element1,element2))

    def wipe_down_element(self, element):
        """
        向下滑动到某个元素
        :return:
        """
        # is_find = False
        max_count = 5
        while max_count > 0:
            if self.find_elements(element):
                logger.info("向下滑动到:「{}」".format(element))
            else:
                self.wipe_down()
                max_count -= 1
                logger.info("向下滑动")

    def wipe_up_element(self, element):
        """
        向上滑动到某个元素
        :return:
        """
        # is_find = False
        max_count = 10
        while max_count > 0:
            if self.find_elements(element):
                logger.info("向上滑动到:「{}」".format(element))
            else:
                self.wipe_up()
                max_count -= 1
                logger.info("向上滑动")

    def back(self):
        """
        模拟物理键返回
        :return:
        """
        self.d.press("back")
        logger.info("点击返回")

    def toast_show(self, text, duration=5):
        """
        页面出现弹窗提示时间，默认时间5s
        :param text:弹窗内容
        :param duration:弹窗提示时间
        :return:
        """
        self.d.toast.show(text, duration)
        logger.info("展示文字")

    def assert_get_toast_message(self,toast_content):
        """
        页面出现toast提示时间，默认时间5s
        :param text:弹窗内容
        :return:
        """
        assert toast_content in self.d.toast.get_message(5.0, default="")
        logger.info("获取toast内容:「{}」".format(toast_content))

    def wait_element_appear(self, element, log_text, timeout=5):
        """
        等待某个元素的出现，默认等待时间5s
        :param element: 元素内容
        :param log_text:log元素内容
        :param timeout:超时时间
        :return:
        """
        self.d(text=element).wait(timeout=timeout)
        logger.info("等待「{}」元素出现".format(log_text))

    def wait_element_gone(self, element, log_text, timeout=2):
        """
        等待某个元素的消失，默认等待时间5s
        :param element: 元素内容
        :param log_text:log元素内容
        :param timeout:超时时间
        :return:
        """
        self.d(text=element).wait_gone(timeout=timeout)
        logger.info("等待「{}」元素消失".format(log_text))

    def find_elements(self, element, timeout=5):
        """
        查找元素是否存在当前页面
        :param element: 元素内容
        :param timeout:log元素内容
        :return:
        """
        is_exist = False
        try:
            while timeout > 0:
                xml = self.d.dump_hierarchy()
                if re.findall(element, xml):
                    is_exist = True
                    logger.info("查询到「{}」".format(element))
                    break
                else:
                    timeout -= 1
        except Exception as e:
            logger.info("「{}」查找失败!「{}」".format(element, e))
        finally:
            return is_exist

    def elements_exist(self, element):
        """
        断言当前页面元素情况，用于判断多个页面状态的判断
        :param element:
        :return:
        """
        is_exist = False
        if self.d(text=element).exists(timeout=5):
            is_exist = True
        return is_exist

    def elements_exist(self, element1,element2):
        """
        断言当前页面元素情况，用于判断多个页面状态的判断
        :param element1: resourceId
        :param element2: text
        :return:
        """
        is_exist = False
        if self.d(resourceId=element1,text=element2).exists(timeout=5):
            is_exist = True
        return is_exist

    def assert_exist(self, element):
        """
        断言当前页面存在要查找的元素,存在则判断成功
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(text=element).exists(timeout=5) == True, "断言「{}」元素存在,失败了!".format(element)
        logger.info("断言「{}」元素存在,成功了!".format(element))

    def assert_textContains_exist(self, element):
        """
        模糊查询页面存在text,存在则判断成功
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(textContains=element).exists(timeout=5) == True, "断言「{}」元素存在,失败了!".format(element)
        logger.info("断言「{}」元素存在,成功了!".format(element))

    def assert_element_exist(self, element):
        """
        断言当前页面存在要查找的元素,存在则判断成功
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(resourceId=element).exists(timeout=5) == True, "断言「{}」元素存在,失败了!".format(element)
        logger.info("断言「{}」元素存在,成功了!".format(element))

    def assert_element_xpath_exist(self, element):
        """
        断言当前页面存在要查找的xpath元素,存在则判断成功
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(xpath=element).exists(timeout=5) == True, "断言「{}」元素存在,失败了!".format(element)
        logger.info("断言「{}」元素存在,成功了!".format(element))

    def assert_element_description_exist(self, element):
        """
        断言当前页面存在要查找的description元素,存在则判断成功
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(description=element).exists(timeout=5) == True, "断言「{}」元素存在,失败了!".format(element)
        logger.info("断言「{}」元素存在,成功了!".format(element))

    def assert_not_exist(self, element):
        """
        假设三秒走满 还没有找到这个页面有这个元素 判断这个页面元素不存在
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        start_time = time.time()
        self.d(text=element).exists(timeout=10)
        end_time = time.time()
        assert (end_time - start_time > 3) == True,"断言「{}」元素不存在,失败了!".format(element)
        logger.info("断言「{}」元素不存在,成功了!".format(element))

    def assert_contain_text(self, localtion, element):
        """
        断言页面的某个位置是否含有该文字
        :param localtion: 直接是x,y 坐标
        :param element:
        :return:
        """
        element_details = self.d(localtion).info
        assert element == element_details["text"], "断言「{}」位置没有「{}」元素失败!".format(localtion, element)
        logger.info("断言「{}」位置存在「{}」元素成功!".format(localtion, element))

    def wait_time(self, timeout=2):
        time.sleep(timeout)

    def assert_image_findit(self, image_url):
        """
        断言页面的是否含有该图片
        :param pic: 图片的路径
        :return:
        """
        image_dict = self.d.image.match(image_url)
        assert image_dict['similarity'] >= 0.99,"断言「{}」图片元素不存在!".format(image_url)
        logger.info("断言「{}」图片元素存在!".format(image_url))

    def assert_not_image_findit(self, image_url):
        """
        断言页面的是否含有该图片
        :param pic: 图片的路径
        :return:
        """
        image_dict = self.d.image.match(image_url)
        assert image_dict['similarity'] < 0.99,"断言{}图片元素存在,为{}!".format(image_url,image_dict['similarity'])
        logger.info("断言{}图片不元素存在,相似度为{}!".format(image_url,image_dict['similarity']))

    def click_image_findit(self, image_url):
        """
        点击当前页面的该图片
        :param pic: 图片的路径
        :return:
        """
        self.d.image.click(image_url,timeout=20.0)
        logger.info("点击元素:「{}」".format(image_url))

    def save_element_screenshot_description(self,save_url, element, pic_name):
        """
        保存元素定位的图片
        :param pic: 图片的路径
        :return:
        """
        im = self.d(description=element).screenshot()
        im.save(save_url)
        logger.info("保存{}图片到aseert_pic目录下".format(pic_name))

    def get_element_text(self, element):
        """
        获取当前元素的text
        :param element: 元素定位
        :return:
        """
        element_text = self.d(resourceId=element).get_text()
        logger.info("元素:「{}」的text为「{}」".format(element,element_text))
        return element_text
