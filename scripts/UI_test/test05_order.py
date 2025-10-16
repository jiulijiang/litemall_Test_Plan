import os
import sys
import pytest

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

from UI.Mod02_usrLogin import UserLogin
from UI.Mod04_Cart import Cart
from UI.Mod05_order import Order
from UI.wd_init import WD_init
from common.utils import read_json_as_dict


class TestOrder:
    """订单模块测试类"""
    

    def setup_method(self):
        """方法级别的前置方法"""
        # 初始化浏览器
        self.wd = WD_init()
        # 最大化浏览器窗口
        # 实例化订单模块
        self.order = Order()
        # 实例化购物车模块
        self.cart = Cart()
        self.wd.maximize_window()
    
    def teardown_method(self):
        """方法级别的后置方法"""
        # 关闭浏览器
        if hasattr(self, 'wd'):
            self.wd.quit()

    
    @pytest.mark.parametrize("test_case", read_json_as_dict('date/UI/order_cases.json'))
    def test_create_order(self, test_case):

        
        try:
            case_id = test_case['case_id']
            case_title = test_case['case_title']
            screenshot_num = test_case['screenshot_num']
            order_remark = test_case['order_remark']
            select_address = test_case['select_address']
            cart_empty = test_case.get('cart_empty', False)
            expected_result = test_case['expected_result']

            # 执行差异化添加商品至购物车操作
            if  not cart_empty:
                # 添加商品至购物车
                self.cart.add_cart(self.wd, 1, 1)
            else:
                # 只登录
                self.Login = UserLogin()
                self.Login.login(self.wd, config.USER_NAME, config.USER_PASSWORD)
            # 调用创建订单方法
            self.order.create_order(self.wd,order_remark, select_address,screenshot_num,cart_empty)

            # 截图以便后期检查页面上是否显示了预期的提示信息
            print(f"测试用例{case_id}({case_title})执行完成，截图已保存")
            print(f"预期结果: {expected_result}")

            # 断言预期结果列表中是否有任意一个字符串包含在页面源代码中
            assert any(result in self.wd.page_source for result in expected_result), \
                f"测试用例{case_id}({case_title})失败，预期结果列表中的任何字符串都未在页面中找到: {expected_result}"
            
        except Exception as e:
            # 捕获异常并打印
            print(f"测试用例 {test_case['case_id']} - {test_case['case_title']}: 执行出错 - {str(e)}")
            # 抛出异常使测试失败
            raise


if __name__ == "__main__":
    # 直接运行测试
    pytest.main(["-v", "test05_order.py"])