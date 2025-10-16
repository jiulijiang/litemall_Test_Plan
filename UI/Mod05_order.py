import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UI.wd_init import WD_init
from UI.Mod04_cart import Cart


class Order:
    """
    订单模块
    """
    def __init_order(self,wd: webdriver):
        """"
        初始化订单
        """
        Cart().add_cart(wd, 1, 1)

    def create_order(self, wd: webdriver, SCREENSHOT_NUM: int = 0):
        """"
        创建订单
        """
        # 初始化前置条件
        self.__init_order(wd)
        # 点击购物车

        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-goods-action-icon:nth-child(1)')).click()
        time.sleep(1)
        # 点击去结算
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-button:nth-child(3)')).click()
        time.sleep(0.5)

        # 点击选择地址
        WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.van-cell--clickable'))[0].click()
        time.sleep(0.5)

        # 选择具体地址
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-address-item:nth-child(1)')).click()
        time.sleep(0.5)

        # 点击提交
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-button--normal')).click()
        time.sleep(0.5)

        # 截图
        if SCREENSHOT_NUM != 0:
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test05-createOrder\\createOrder{SCREENSHOT_NUM}.png")



if __name__ == "__main__":
    order = Order()
    wd = WD_init()
    order.create_order(wd, 1)
    wd.close()