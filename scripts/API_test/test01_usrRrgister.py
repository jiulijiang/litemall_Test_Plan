import os
import sys
import unittest
import logging
import os

import pytest

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 导入必要的模块
from api.Litemall_API import LiteMallAPI


class TestUserRegister(unittest.TestCase):
    """
    测试用户注册接口
    """

    def setup_method(self):
        """
        初始化API方法实例
        """
        self.api = LiteMallAPI()

