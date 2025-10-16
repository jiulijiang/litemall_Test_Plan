import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UI.wd_init import WD_init

class UserRegister:
    """
    用户注册模块
    """

    def register(self, wd: webdriver,USER_PHONE: str,CODE:str,USER_NAME: str,
                 USER_PASSWORD: str,RE_USER_PASSWORD:str,SCREENSHOT_NUM: int,CASE_TITLE: str):
        """
        用户注册
        """
        # 点击我的
        wd.find_element(By.CSS_SELECTOR, ".van-tabbar-item:nth-child(4)").click()
        time.sleep(0.5)
        # 点击注册
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '[href="#/login/registerGetCode"]')).click()
        time.sleep(0.5)
        # 输入手机号
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input')).send_keys(USER_PHONE)
        #  点击下一步
        wd.find_element(By.CSS_SELECTOR, ".van-button").click()
        time.sleep(0.5)
        # 判断用例是否为手机号测试用例
        if "手机号" in CASE_TITLE:
            # 手机号测试用例在此处截屏
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test01-register\\register{SCREENSHOT_NUM}.png")
            # 提前结束
            return None

        # 输入注册信息
        register_inputs = WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, 'input[type]'))
        register_inputs[0].send_keys(CODE)
        register_inputs[1].send_keys(USER_NAME)
        register_inputs[2].send_keys(USER_PASSWORD)
        register_inputs[3].send_keys(RE_USER_PASSWORD)
        # 点击注册
        wd.find_element(By.CSS_SELECTOR, ".van-button").click()
        time.sleep(0.5)
        # 截图获取结果
        time.sleep(1)
        wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test01-register\\register{SCREENSHOT_NUM}.png")





if __name__ == "__main__":
    register = UserRegister()
    wd = WD_init()
    register.register(wd, "13611225855", "665666", "jack101", "123456", 1)
    wd.close()