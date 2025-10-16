import os
import sys
import pytest

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from UI.Mod04_Cart import Cart
from UI.wd_init import WD_init
from common.utils import read_json_as_dict
from selenium.webdriver.common.by import By

class TestCart:
    """购物车模块测试类"""
    
    def setup_method(self):
        """每个测试方法执行前的初始化方法"""
        # 初始化WebDriver
        self.wd = WD_init()
        # 实例化购物车类
        self.cart = Cart()
    
    def teardown_method(self):
        """每个测试方法执行后的清理方法"""
        # 清空购物车，确保后续测试不受到影响
        if self.wd:
            try:
                self.wd.close()
                # 重新初始化WebDriver
                self.wd = WD_init()
                # 执行清除购物车操作
                self.cart = Cart()
                self.cart.clear_cart(self.wd)
                self.wd.close()
            except Exception:
                # 忽略清空购物车过程中可能出现的异常
                pass
            # 关闭浏览器实例
            self.wd.quit()

    
    @pytest.mark.parametrize("test_case", read_json_as_dict('date/UI/cart_cases.json'))
    def test_add_cart(self, test_case):
        """添加购物车测试方法"""


        
        try:

            case_id = test_case['case_id']
            case_title = test_case['case_title']
            spec = test_case['spec']
            goods_num = test_case['goods_num']
            screenshot_num = test_case['screenshot_num']
            expected_result = test_case['expected_result']

            # 执行添加购物车操作
            self.cart.add_cart(self.wd, spec, goods_num, screenshot_num)

            # 截图以便后期检查页面上是否显示了预期的提示信息
            print(f"测试用例{case_id}({case_title})执行完成，截图已保存")
            print(f"预期结果: {expected_result}")

            # 差异化断言-以匹配不同用例需求
            if int(case_id[5:]) <= 10:
                assert any(result in self.wd.find_element(By.CSS_SELECTOR, '.van-info').text for result in expected_result), \
                    f"测试用例{case_id}({case_title})失败，预期结果列表中的任何字符串都未在页面中找到: {expected_result}"
            else:
                assert all(result in self.wd.page_source for result in expected_result), \
                    f"测试用例{case_id}({case_title})失败，预期结果列表中的所有字符串未在页面中找到: {expected_result}"




            print(f"{case_id} - {case_title}: 测试通过")
        except Exception as e:
            print(f"{case_id} - {case_title}: 测试失败，错误信息: {str(e)}")
            raise


if __name__ == "__main__":
    # 直接运行时执行pytest
    pytest.main(["-v", "test04_cart.py"])