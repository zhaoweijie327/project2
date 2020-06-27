from Base.base import BaseDriver
from Page.find_element import FindElement

'''
设置页面定位与操作方法
'''

class SettingPage(BaseDriver):

    # 调用父类BaseDriver初始化方法
    def __init__(self):
        super().__init__()

    # 点解搜索按钮方法
    def click_sousuo(self):
        self.find_click(FindElement.sou_suo)

    # 点击显示方法
    def click_xianshi(self):
        self.find_click(FindElement.setting_xianshi_btn_xpath)

