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
        Ԫ�ص��
        element:Ԫ������
        log_text:��ӡlog���İ�
        xpathʹ�÷���
        1.����
        d.xpath(u"//android.widget.TextView[contains(@text,'���� ?0?6')]").click()
        2.ȫƥ��
        d.xpath(u"//android.widget.TextView[@text='���� ?0?64.99']").click()
        3.ƥ�俪ʼ�ַ�
        d.xpath(u"//android.widget.TextView[starts-with(@text,'���� ?0?6')]").click()
        :return:
        """
        if str(element).startswith("com"):
            self.d(resourceId=element).click()
        elif re.findall("//", str(element)):
            self.d.xpath(element).click()
        else:
            self.d(text=element).click()
        logger.info("���Ԫ��:��{}��".format(log_text))

    def click_text_contains(self,element,log_text):
        """
        ����textԪ�ص��
        element:Ԫ������
        log_text:��ӡlog���İ�
        """
        self.d(textContains=element).click()
        logger.info("���Ԫ��:��{}��".format(log_text))

    def click_description(self, element, log_text):
        """
        descriptionԪ�ص��
        element:Ԫ������
        log_text:��ӡlog���İ�
        """
        self.d(description=element).click()
        logger.info("���Ԫ��:��{}��".format(log_text))

    def click_descriptionContain(self, element, log_text):
        """
        descriptionԪ�ص��
        element:Ԫ������
        log_text:��ӡlog���İ�
        """
        self.d(descriptionContains=element).click()
        logger.info("���Ԫ��:��{}��".format(log_text))

    def click_description_center(self, element):
        """
        ���description�ؼ��м�
        :param element:
        :return:
        """
        x,y = self.d(description=element).center()
        self.d.click(x,y)
        logger.info("���Ԫ�ء�{}��".format(element))

    def send_keys(self, element, sendtext, log_text):
        """
        �ı�����
        element:Ԫ������
        sendtext:������İ�
        log_text:��ӡlog���İ�
        :return:
        """
        if str(element).startswith("com"):
            self.d(resourceId=element).set_text(sendtext)
        elif re.findall("//", str(element)):
            self.d.xpath(element).set_text(sendtext)
        else:
            self.d(text=element).set_text(sendtext)

        logger.info("�������֡�{}��".format(log_text))

    def set_text_contanis(self, element, sendtext, log_text):
        """
        �ı�����
        element:Ԫ������
        sendtext:������İ�
        log_text:��ӡlog���İ�
        :return:
        """
        text_all = self.d(textContains=element).get_text()
        self.d(text=text_all).click()
        self.d.send_keys(sendtext,clear=True)

        logger.info("�������֡�{}��".format(log_text))

    def set_text_FastInputIME(self, sendtext, log_text):
        """
        �ı�����
        sendtext:������İ�
        log_text:��ӡlog���İ�
        :return:
        """
        self.d.send_keys(sendtext,clear=True)
        logger.info("�������֡�{}��".format(log_text))

    def double_click(self, x, y, time=0.5):
        """
        ˫��
        :return:
        """
        self.d.double_click(x, y, time)
        logger.info("�������:��{}��,��{}��".format(x, y))

    def get_window_size(self):
        """
        ��ȡ��Ļ�ߴ�
        :return:
        """
        window_size = self.d.window_size()
        width = int(window_size[0])
        height = int(window_size[1])
        return width, height

    def swipe_up(self, duration=0.5):
        """
        ���ϻ���,�鿴���������
        :return:
        """
        self.d.swipe_ext("up",scale=duration)
        logger.info("���»������鿴���������")

    def swipe_down(self, duration=0.5):
        """
        ���»������鿴���������
        :return:
        """
        self.d.swipe_ext("down",scale=duration)
        logger.info("���»������鿴���������")

    def swipe_left(self, duration=0.5):
        """
        ���󻬶����鿴���������
        :return:
        """
        self.d.swipe_ext("down",scale=duration)
        logger.info("���󻬶����鿴���������")

    def swipe_right(self, duration=0.5):
        """
        ���һ������鿴���������
        :return:
        """
        self.d.swipe_ext("down",scale=duration)
        logger.info("���һ������鿴���������")

    def swipe_x1y1x2y2(self, x1, y1, x2,y2):
        """
        ����ֵ����
        """
        self.d.swipe(x1,y1,x2,y2)
        logger.info("�϶�Ԫ�ء�{}����{}����Ԫ�ء�{}����{}����".format(x1,y1,x2,y2))

    def swipe_to_element(self, element1, element2, duration=0.25):
        """
        ������ĳ��Ԫ��
        :param element1: ��ʼԪ��
        :param element2: Ŀ��Ԫ��
        :param duration: ����ʱ��
        :return:
        """
        self.d(text=element1).drag_to(text=element2, duration=duration)
        logger.info("�϶�Ԫ�ء�{}����Ԫ�ء�{}����".format(element1,element2))

    def wipe_down_element(self, element):
        """
        ���»�����ĳ��Ԫ��
        :return:
        """
        # is_find = False
        max_count = 5
        while max_count > 0:
            if self.find_elements(element):
                logger.info("���»�����:��{}��".format(element))
            else:
                self.wipe_down()
                max_count -= 1
                logger.info("���»���")

    def wipe_up_element(self, element):
        """
        ���ϻ�����ĳ��Ԫ��
        :return:
        """
        # is_find = False
        max_count = 10
        while max_count > 0:
            if self.find_elements(element):
                logger.info("���ϻ�����:��{}��".format(element))
            else:
                self.wipe_up()
                max_count -= 1
                logger.info("���ϻ���")

    def back(self):
        """
        ģ�����������
        :return:
        """
        self.d.press("back")
        logger.info("�������")

    def toast_show(self, text, duration=5):
        """
        ҳ����ֵ�����ʾʱ�䣬Ĭ��ʱ��5s
        :param text:��������
        :param duration:������ʾʱ��
        :return:
        """
        self.d.toast.show(text, duration)
        logger.info("չʾ����")

    def assert_get_toast_message(self,toast_content):
        """
        ҳ�����toast��ʾʱ�䣬Ĭ��ʱ��5s
        :param text:��������
        :return:
        """
        assert toast_content in self.d.toast.get_message(5.0, default="")
        logger.info("��ȡtoast����:��{}��".format(toast_content))

    def wait_element_appear(self, element, log_text, timeout=5):
        """
        �ȴ�ĳ��Ԫ�صĳ��֣�Ĭ�ϵȴ�ʱ��5s
        :param element: Ԫ������
        :param log_text:logԪ������
        :param timeout:��ʱʱ��
        :return:
        """
        self.d(text=element).wait(timeout=timeout)
        logger.info("�ȴ���{}��Ԫ�س���".format(log_text))

    def wait_element_gone(self, element, log_text, timeout=2):
        """
        �ȴ�ĳ��Ԫ�ص���ʧ��Ĭ�ϵȴ�ʱ��5s
        :param element: Ԫ������
        :param log_text:logԪ������
        :param timeout:��ʱʱ��
        :return:
        """
        self.d(text=element).wait_gone(timeout=timeout)
        logger.info("�ȴ���{}��Ԫ����ʧ".format(log_text))

    def find_elements(self, element, timeout=5):
        """
        ����Ԫ���Ƿ���ڵ�ǰҳ��
        :param element: Ԫ������
        :param timeout:logԪ������
        :return:
        """
        is_exist = False
        try:
            while timeout > 0:
                xml = self.d.dump_hierarchy()
                if re.findall(element, xml):
                    is_exist = True
                    logger.info("��ѯ����{}��".format(element))
                    break
                else:
                    timeout -= 1
        except Exception as e:
            logger.info("��{}������ʧ��!��{}��".format(element, e))
        finally:
            return is_exist

    def elements_exist(self, element):
        """
        ���Ե�ǰҳ��Ԫ������������ж϶��ҳ��״̬���ж�
        :param element:
        :return:
        """
        is_exist = False
        if self.d(text=element).exists(timeout=5):
            is_exist = True
        return is_exist

    def elements_exist(self, element1,element2):
        """
        ���Ե�ǰҳ��Ԫ������������ж϶��ҳ��״̬���ж�
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
        ���Ե�ǰҳ�����Ҫ���ҵ�Ԫ��,�������жϳɹ�
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(text=element).exists(timeout=5) == True, "���ԡ�{}��Ԫ�ش���,ʧ����!".format(element)
        logger.info("���ԡ�{}��Ԫ�ش���,�ɹ���!".format(element))

    def assert_textContains_exist(self, element):
        """
        ģ����ѯҳ�����text,�������жϳɹ�
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(textContains=element).exists(timeout=5) == True, "���ԡ�{}��Ԫ�ش���,ʧ����!".format(element)
        logger.info("���ԡ�{}��Ԫ�ش���,�ɹ���!".format(element))

    def assert_element_exist(self, element):
        """
        ���Ե�ǰҳ�����Ҫ���ҵ�Ԫ��,�������жϳɹ�
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(resourceId=element).exists(timeout=5) == True, "���ԡ�{}��Ԫ�ش���,ʧ����!".format(element)
        logger.info("���ԡ�{}��Ԫ�ش���,�ɹ���!".format(element))

    def assert_element_xpath_exist(self, element):
        """
        ���Ե�ǰҳ�����Ҫ���ҵ�xpathԪ��,�������жϳɹ�
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(xpath=element).exists(timeout=5) == True, "���ԡ�{}��Ԫ�ش���,ʧ����!".format(element)
        logger.info("���ԡ�{}��Ԫ�ش���,�ɹ���!".format(element))

    def assert_element_description_exist(self, element):
        """
        ���Ե�ǰҳ�����Ҫ���ҵ�descriptionԪ��,�������жϳɹ�
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(description=element).exists(timeout=5) == True, "���ԡ�{}��Ԫ�ش���,ʧ����!".format(element)
        logger.info("���ԡ�{}��Ԫ�ش���,�ɹ���!".format(element))

    def assert_not_exist(self, element):
        """
        ������������ ��û���ҵ����ҳ�������Ԫ�� �ж����ҳ��Ԫ�ز�����
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        start_time = time.time()
        self.d(text=element).exists(timeout=10)
        end_time = time.time()
        assert (end_time - start_time > 3) == True,"���ԡ�{}��Ԫ�ز�����,ʧ����!".format(element)
        logger.info("���ԡ�{}��Ԫ�ز�����,�ɹ���!".format(element))

    def assert_contain_text(self, localtion, element):
        """
        ����ҳ���ĳ��λ���Ƿ��и�����
        :param localtion: ֱ����x,y ����
        :param element:
        :return:
        """
        element_details = self.d(localtion).info
        assert element == element_details["text"], "���ԡ�{}��λ��û�С�{}��Ԫ��ʧ��!".format(localtion, element)
        logger.info("���ԡ�{}��λ�ô��ڡ�{}��Ԫ�سɹ�!".format(localtion, element))

    def wait_time(self, timeout=2):
        time.sleep(timeout)

    def assert_image_findit(self, image_url):
        """
        ����ҳ����Ƿ��и�ͼƬ
        :param pic: ͼƬ��·��
        :return:
        """
        image_dict = self.d.image.match(image_url)
        assert image_dict['similarity'] >= 0.99,"���ԡ�{}��ͼƬԪ�ز�����!".format(image_url)
        logger.info("���ԡ�{}��ͼƬԪ�ش���!".format(image_url))

    def assert_not_image_findit(self, image_url):
        """
        ����ҳ����Ƿ��и�ͼƬ
        :param pic: ͼƬ��·��
        :return:
        """
        image_dict = self.d.image.match(image_url)
        assert image_dict['similarity'] < 0.99,"����{}ͼƬԪ�ش���,Ϊ{}!".format(image_url,image_dict['similarity'])
        logger.info("����{}ͼƬ��Ԫ�ش���,���ƶ�Ϊ{}!".format(image_url,image_dict['similarity']))

    def click_image_findit(self, image_url):
        """
        �����ǰҳ��ĸ�ͼƬ
        :param pic: ͼƬ��·��
        :return:
        """
        self.d.image.click(image_url,timeout=20.0)
        logger.info("���Ԫ��:��{}��".format(image_url))

    def save_element_screenshot_description(self,save_url, element, pic_name):
        """
        ����Ԫ�ض�λ��ͼƬ
        :param pic: ͼƬ��·��
        :return:
        """
        im = self.d(description=element).screenshot()
        im.save(save_url)
        logger.info("����{}ͼƬ��aseert_picĿ¼��".format(pic_name))

    def get_element_text(self, element):
        """
        ��ȡ��ǰԪ�ص�text
        :param element: Ԫ�ض�λ
        :return:
        """
        element_text = self.d(resourceId=element).get_text()
        logger.info("Ԫ��:��{}����textΪ��{}��".format(element,element_text))
        return element_text
