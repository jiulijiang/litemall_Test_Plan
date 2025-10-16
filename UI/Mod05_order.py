import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UI.wd_init import WD_init
from UI.Mod04_Cart import Cart


class Order:
    """
    订单模块
    """


    def create_order(self, wd: webdriver,ORDER_REMARKS:str,select_address: bool, SCREENSHOT_NUM: int = 0,cart_empty:bool =  False):
        """"
        创建订单
        """
        # 差异化选择购物车
        if cart_empty:
            # 用户界面选择购物车
            WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-tabbar-item:nth-child(3)')).click()
        else:
            # 商品界面点击购物车
            WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-goods-action-icon:nth-child(1)')).click()
        time.sleep(1)
        # 点击去结算
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-button:nth-child(3)')).click()
        # 空购物车在此处结束并截屏
        if cart_empty:
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test05-createOrder\\createOrder{SCREENSHOT_NUM}.png")
            return None
        time.sleep(0.5)
        # 判断是否选择地址
        if select_address:
            # 点击选择地址
            WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.van-cell--clickable'))[0].click()
            time.sleep(0.5)

            # 选择具体地址
            WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-address-item:nth-child(1)')).click()
            time.sleep(0.5)
        # 填写订单备注
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, 'input')).send_keys(ORDER_REMARKS)
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
    Cart().add_cart(wd, 1, 1)
    order.create_order(wd, "1")
    wd.close()