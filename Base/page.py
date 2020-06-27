'''
实例化管理Page包的页面方法
'''
from Page.setting_page import SettingPage
from Page.sousuo_page import SouSuoPage
from Page.xianshi_page import XianShiPage


class Page_Administration:

    # 设置页面
    @classmethod
    def setting(cls):
        return SettingPage()

    # 搜索页面
    @classmethod
    def sousuo(cls):
        return SouSuoPage()

    # 显示页面
    @classmethod
    def xianshi(cls):
        return XianShiPage()