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

class Address:
    """
    地址模块
    """
    def __init_address(self,wd: webdriver):
        """
        初始化地址
        """
        UserLogin().login(wd, config.USER_NAME, config.USER_PASSWORD)


    def add_address(self, wd: webdriver, USER_NAME: str, USER_PHONE: str, USER_ADDRESS: str,
                    PROVINCE: str = "北京市" ,CITY: str = "市辖区",DISTRICT: str = "西城区",
                    is_default: bool = False,SCREENSHOT_NUM: int = 0):
        """
        添加地址
        """
        # 初始化前置条件
        self.__init_address(wd)
        # 点击地址
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, 'div:nth-child(2).van-cell--clickable')).click()
        time.sleep(0.5)
        # 点击新增地址
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-button--normal')).click()
        time.sleep(0.5)
        # 姓名，手机号
        WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, 'input'))[0].send_keys(USER_NAME)
        WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, 'input'))[1].send_keys(USER_PHONE)
        time.sleep(0.5)
        # 地址选择
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-cell--clickable')).click()
        time.sleep(1)  # 等待动画结束
        # 选择省
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.XPATH, f"//*[text()='{PROVINCE}']")).click()  # xpth可以根据文字选择
        time.sleep(1)  # 等待滚动动画
        # 选择市
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.XPATH, f"//*[text()='{CITY}']")).click()
        time.sleep(1)
        # 选择区
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.XPATH, f"//*[text()='{DISTRICT}']")).click()
        time.sleep(1)
        # 点击确定
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-picker__confirm')).click()

        # 填写详细地址
        WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, 'textarea')).send_keys(USER_ADDRESS)
        time.sleep(0.5)
        # 是否为默认地址
        if is_default:
            WebDriverWait(wd,5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.van-switch:nth-child(1)')).click()

        # 点击保存
        WebDriverWait(wd,5).until(lambda x: x.find_elements(By.CSS_SELECTOR, '.van-button--block'))[0].click()
        time.sleep(0.5)

        # 截图
        if SCREENSHOT_NUM != 0:
            time.sleep(1)
            wd.get_screenshot_as_file(config.BASE_DIR+f"\\screenshots\\test06-addAddress\\addAddress{SCREENSHOT_NUM}.png")



if __name__ == "__main__":
    address = Address()
    wd = WD_init()
    address.add_address(wd, "jack", "13611225855", "西城区德胜门外大街1号", is_default=True, SCREENSHOT_NUM=1)
    wd.close()