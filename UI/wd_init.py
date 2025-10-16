import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


from selenium import webdriver


def WD_init(URL: str = config.BASE_URL_USR):
    """
    初始化浏览器对象
    """
    wd = webdriver.Edge()
    wd.get(URL)
    wd.maximize_window()
    return wd