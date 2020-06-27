import os
import yaml
from appium import webdriver


class Driver:

    __driver = None

    # 声明驱动
    @classmethod
    def driver_open(cls):
        if cls.__driver is None:
            # server 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明我们的driver对象
            cls.__driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.__driver
        else:
            return cls.__driver

    # 关闭驱动
    @classmethod
    def driver_close(cls):
        if cls.__driver:
            cls.driver_open().quit()
            cls.__driver = None

# 数据传输
class Data:
    @classmethod
    def path_file(cls,filepath):
        '''读数据'''
        data_list = []
        with open(filepath,'r',encoding='utf-8') as file:
            # 使用yaml加载数据
            data = yaml.safe_load(file)
            for i in data.values():
                data_list.append(tuple(i.values()))

        return data_list

BAR_LUJING = os.path.abspath(os.path.dirname(__file__))