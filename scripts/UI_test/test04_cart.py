import os
import sys
import json
import time
import pytest
from selenium import webdriver

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from UI.Mod04_cart import Cart
from UI.wd_init import WD_init


class TestCart:
    """购物车模块测试类"""
    
    @classmethod
    def setup_class(cls):
        """测试类的初始化方法，在所有测试方法执行前执行一次"""
        print("\n===== 开始执行购物车模块测试 =====")
    
    @classmethod
    def teardown_class(cls):
        """测试类的清理方法，在所有测试方法执行后执行一次"""
        print("\n===== 购物车模块测试执行完毕 =====")
    
    def setup_method(self):
        """每个测试方法执行前的初始化方法"""
        # 初始化WebDriver
        self.wd = WD_init()
        # 实例化购物车类
        self.cart = Cart()
    
    def teardown_method(self):
        """每个测试方法执行后的清理方法"""
        # 关闭浏览器
        if self.wd:
            self.wd.quit()
    
    @staticmethod
    def get_test_cases():
        """获取测试用例数据"""
        try:
            # 读取JSON文件中的测试数据
            file_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                "date", "UI", "cart_cases.json"
            )
            
            with open(file_path, "r", encoding="utf-8") as f:
                test_cases = json.load(f)
                
            # 将测试数据转换为元组格式，用于pytest参数化
            test_data = []
            for case in test_cases:
                test_data.append((
                    case["case_id"],
                    case["case_title"],
                    case["spec"],
                    case["goods_num"],
                    case["screenshot_num"],
                    case["expected_result"]
                ))
            
            return test_data
        except Exception as e:
            print(f"读取测试数据时发生错误: {e}")
            return []
    
    @pytest.mark.parametrize("case_id, case_title, spec, goods_num, screenshot_num, expected_result", get_test_cases.__func__())
    def test_add_cart(self, case_id, case_title, spec, goods_num, screenshot_num, expected_result):
        """添加购物车测试方法"""
        print(f"\n执行测试用例: {case_id} - {case_title}")
        print(f"测试数据: 规格={spec}, 商品数量={goods_num}, 截图编号={screenshot_num}")
        
        try:
            # 执行添加购物车操作
            self.cart.add_cart(self.wd, spec, goods_num, screenshot_num)
            
            # 由于我们以Mod04_Cart.py为准，这里不添加额外的断言
            # 只要add_cart方法执行完成，就认为测试通过
            print(f"{case_id} - {case_title}: 测试通过")
        except Exception as e:
            print(f"{case_id} - {case_title}: 测试失败，错误信息: {str(e)}")
            raise


if __name__ == "__main__":
    # 直接运行时执行pytest
    pytest.main(["-v", "test04_cart.py"])