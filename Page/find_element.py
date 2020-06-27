from selenium.webdriver.common.by import By

'''
集中管理元素属性

'''

class FindElement:

    # -----------------设置页面-----------------
    # 定位搜索按钮
    sou_suo = (By.ID, 'com.android.settings:id/search')
    # 点击显示
    setting_xianshi_btn_xpath = (By.XPATH, "//*[contains(@text,'显示')]")

    # -----------------搜索页面-----------------
    # 定位输入框输入内容
    send = (By.ID, 'android:id/search_src_text')
    # 获取结果
    duanyan = (By.ID, "com.android.settings:id/title")

    # -----------------显示页面-----------------
    # 字体大小
    xianshi_ziti_dx_xpath = (By.XPATH, "//*[contains(@text,'字体大小')]")
    # 选择字体
    xianshi_choice_pt_xpath = (By.XPATH, "//*[contains(@text,'普通')]")
    # 描述信息
    xianshi_get_summary_ids = (By.ID, "android:id/summary")