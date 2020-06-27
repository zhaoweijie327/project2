from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver

'''
封装元素定位方法
操作方法
'''

class BaseDriver:

    # 初始化Driver驱动
    def __init__(self):
        self.driver = Driver().driver_open()

    # 定位单个元素方法
    def find_ele(self,loc):
        '''
        定位单个元素方法
        :param loc: By,ID.属性值、By,CLASS_NAME.属性值、By,XPATH.属性值
        :return:
        '''
        return self.driver.find_element(*loc)

    # 定位一组元素
    def find_eles(self,loc):
        '''
        定位一组元素方法
        :param loc: By,ID.属性值、By,CLASS_NAME.属性值、By,XPATH.属性值
        :return:
        '''
        return self.driver.find_elements(*loc)

    # 显示等待定位单个元素
    def find_ele_wait(self,loc,waittime=5,timewait=1.0):
        '''
        显示等待定位单个元素
        :param loc: By,ID.属性值、By,CLASS_NAME.属性值、By,XPATH.属性值
        :param waittime: 定位元素等待5秒
        :param timewait: 查找元素间隔时间1秒
        :return:
        '''
        return WebDriverWait(self.driver,waittime,timewait).until(lambda x : x.find_element(*loc))

    # 显示等待定位一组元素
    def find_eles_wait(self,loc,waittime=5,timewait=1.0):
        '''
        显示等待定位一组元素
        :param loc: By,ID.属性值、By,CLASS_NAME.属性值、By,XPATH.属性值
        :param waittime: 定位元素等待5秒
        :param timewait: 查找元素间隔时间1秒
        :return:
        '''
        return WebDriverWait(self.driver,waittime,timewait).until(lambda x : x.find_elements(*loc))

    # 点击方法
    def find_click(self,loc):
        self.find_ele_wait(loc).click()

    # 输入方法
    def find_send(self,loc,text):
        self.find_ele_wait(loc).send_keys(text)