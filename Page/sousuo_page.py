from Base.base import BaseDriver
from Page.find_element import FindElement

'''
设置页面定位与操作方法
'''

class SouSuoPage(BaseDriver):

    # 调用父类BaseDriver初始化方法
    def __init__(self):
        super().__init__()

    # 点解搜索按钮方法
    def send_text(self,text):
        self.find_send(FindElement.send,text)

    # 获取详情信息
    def get_text(self):
        results = self.find_eles_wait(FindElement.duanyan)
        return [i.text for i in results]