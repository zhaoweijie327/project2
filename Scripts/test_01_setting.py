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

    @pytest.mark.parametrize("search_data, exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_setting_01(self,search_data,exp_data):

        # 点击设置页面的搜索
        Page_Administration.setting().click_sousuo()

        # 搜索页面 输入内容
        Page_Administration.sousuo().send_text(search_data)
        # 获取信息并断言
        assert exp_data in Page_Administration.sousuo().get_text()