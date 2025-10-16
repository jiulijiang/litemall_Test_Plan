import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UI.wd_init import WD_init

class GoodsSearch:
    """
    商品搜索模块
    """
    def search(self, wd: webdriver,KEYWORD: str,SCREENSHOT_NUM: int = 0):
        """
        商品搜索
        """
        # 点击首页
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-tabbar-item:nth-child(1)')).click()
        time.sleep(0.5)
        # 输入搜索关键字
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input')).click()
        time.sleep(0.5)
        WebDriverWait(wd, 5).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input')).send_keys(KEYWORD + '\n')

        # 截图
        if SCREENSHOT_NUM != 0:
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test03-search\\search{SCREENSHOT_NUM}.png")



if __name__ == "__main__":
    search = GoodsSearch()
    wd = WD_init()
    search.search(wd, "母亲节", 1)