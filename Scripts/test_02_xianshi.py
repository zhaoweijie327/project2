'''
管理测试用例

'''
import pytest

from Base.driver import Driver
from Base.page import Page_Administration


class Test_Setting:

    def setup_class(self):
        pass

    def teardown_class(self):
        # 关闭驱动
        Driver().driver_close()

    def test_xianshi_02(self):

        # 点击设置页面的显示
        Page_Administration.setting().click_xianshi()

        # 显示页面 点击字体大小
        Page_Administration.xianshi().click_daxiao()
        # 显示页面 选择字体类型
        Page_Administration.xianshi().click_ziti()
        assert '普通' in Page_Administration.xianshi().get_xinxi()