from Base.base import BaseDriver
from Page.find_element import FindElement

'''
设置页面定位与操作方法
'''

class XianShiPage(BaseDriver):

    # 调用父类BaseDriver初始化方法
    def __init__(self):
        super().__init__()

    # 点击字体大小
    def click_daxiao(self):
        self.find_click(FindElement.xianshi_ziti_dx_xpath)

    # 点击字体类型
    def click_ziti(self):
        self.find_click(FindElement.xianshi_choice_pt_xpath)

    # 获取断言信息
    def get_xinxi(self):
        results = self.find_eles_wait(FindElement.xianshi_get_summary_ids)
        return [i.text for i in results]