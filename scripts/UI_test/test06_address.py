import os
import sys
import pytest
import time

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from UI.wd_init import WD_init
from UI.Mod06_address import Address
from common.utils import read_json_as_dict


class TestAddress:
    """地址管理模块测试类"""

    
    def setup_method(self):
        # 初始化浏览器
        self.wd = WD_init()
        self.address = Address()
        # 最大化浏览器窗口
        self.wd.maximize_window()

    
    def teardown_method(self):
        # 关闭浏览器
        if hasattr(self, 'wd'):
            self.wd.quit()
    
    @pytest.mark.parametrize("test_case", read_json_as_dict('date/UI/address_cases.json'))
    def test_add_address(self, test_case):
        """测试添加地址功能"""


        try:
            # 调用添加地址方法
            case_id=test_case['case_id']
            case_title=test_case['case_title']
            user_name=test_case['user_name']
            user_phone=test_case['user_phone']
            user_address=test_case['user_address']
            province=test_case['province']
            city=test_case['city']
            district=test_case['district']
            is_default=test_case['is_default']
            screenshot_num=test_case['screenshot_num']
            expected_result=test_case['expected_result']
            choose_address=test_case.get('choose_address', True)


            # 调用添加地址方法
            self.address.add_address(
                wd=self.wd,
                USER_NAME=user_name,
                USER_PHONE=user_phone,
                USER_ADDRESS=user_address,
                PROVINCE=province,
                CITY=city,
                DISTRICT=district,
                is_default=is_default,
                CHOOSE_ADDRESS=choose_address,
                SCREENSHOT_NUM=screenshot_num
            )

            # 截图以便后期检查页面上是否显示了预期的提示信息
            print(f"测试用例{case_id}({case_title})执行完成，截图已保存")
            print(f"预期结果: {expected_result}")
            
            # 断言预期结果列表中是否有任意一个字符串包含在页面源代码中
            assert any(result in self.wd.page_source for result in expected_result), \
                f"测试用例{case_id}({case_title})失败，预期结果列表中的任何字符串都未在页面中找到: {expected_result}"



        except Exception as e:
            print(f"测试用例{case_id}({case_title})执行失败: {str(e)}")
            raise


if __name__ == "__main__":
    # 直接运行测试
    pytest.main(["-v", "test06_address.py"])