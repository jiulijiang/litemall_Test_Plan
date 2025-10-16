import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UI.wd_init import WD_init
from UI.Mod02_usrLogin import UserLogin
from UI.Mod03_goodsSearch import GoodsSearch


class Cart:
    """"
    购物车模块
    """
    def __init_cart(self,wd: webdriver):
        """
        初始化购物车
        """
        UserLogin().login(wd, config.USER_NAME, config.USER_PASSWORD)
        GoodsSearch().search(wd, "母亲节")


    def add_cart(self, wd: webdriver,SPEC: int,GOODS_NUM: int,SCREENSHOT_NUM: int = 0):
        """
        添加购物车
        """
        # 初始化前置条件
        self.__init_cart(wd)

        # 点击商品
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-card:nth-child(1)')).click()

        # 点击加入购物车
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-button:nth-child(3)')).click()
        time.sleep(0.5) # 等待动画结束
        # 选择规格
        spec_choose = WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.van-sku-row__item'))
        time.sleep(0.5)
        # SPEC 转临时变量
        spec = SPEC
        if spec < 3 :
            spec_choose[0].click()
            time.sleep(0.5)
        else:
            spec_choose[1].click()
            time.sleep(0.5)
            spec = spec - 3
        if spec == 1:
            spec_choose[2].click()
            time.sleep(0.5)
        elif spec == 2:
            spec_choose[3].click()
            time.sleep(0.5)
        elif spec == 3:
            spec_choose[4].click()
            time.sleep(0.5)



        # 填写数量
        wd.find_element(By.CSS_SELECTOR, 'input').send_keys(GOODS_NUM)
        time.sleep(0.5)
        # 点击加入购物车
        wd.find_element(By.CSS_SELECTOR, '.van-button--large:nth-child(1)').click()
        time.sleep(0.5)
        # 截图
        if SCREENSHOT_NUM != 0:
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test04-addCart\\addCart{SCREENSHOT_NUM}.png")

if __name__ == "__main__":
    cart = Cart()
    cart.wd = WD_init()
    cart.add_cart(cart.wd, 1, 1, 1)