import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UI.wd_init import WD_init

class UserLogin():
    """
    用户登录模块
    """
    def login(self, wd: webdriver,USER_NAME: str,USER_PASSWORD: str,SCREENSHOT_NUM: int = 0):
        """
        登录
        """
        # 点击我的
        wd.find_element(By.CSS_SELECTOR, ".van-tabbar-item:nth-child(4)").click()
        time.sleep(0.5)
        # 输入账号密码
        usr_inputs = WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, 'input'))
        usr_inputs[0].send_keys(USER_NAME)
        usr_inputs[1].send_keys(USER_PASSWORD)

        # 点击登录
        wd.find_element(By.CSS_SELECTOR, ".van-button").click()
        time.sleep(0.5)

        # 截图
        if SCREENSHOT_NUM != 0:
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test02-login\\login{SCREENSHOT_NUM}.png")


if __name__ == "__main__":
    login = UserLogin()
    wd = WD_init()
    login.login(wd, "jack0011", "123456", 1)
    wd.close()