import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from UI.wd_init import WD_init
from UI.Mod02_usrLogin import UserLogin
from common.utils import read_json_as_dict

class TestUserLogin:
    """
    用户登录模块测试类
    """

    
    def setup_method(self):
        """
        每个测试方法执行前的设置
        """
        # 初始化浏览器
        self.wd = WD_init()
        # 初始化登录类
        self.login = UserLogin()
    
    def teardown_method(self):
        """
        每个测试方法执行后的清理
        """
        # 关闭浏览器
        if hasattr(self, 'wd') and self.wd:
            self.wd.close()
    

    
    @pytest.mark.parametrize('test_case',read_json_as_dict('date/UI/login_cases.json') )
    def test_user_login(self, test_case):
        """
        用户登录模块参数化测试
        """
        try:
            # 提取测试数据
            case_id = test_case['case_id']
            case_title = test_case['case_title']
            user_name = test_case['user_name']
            user_password = test_case['user_password']
            screenshot_num = test_case['screenshot_num']
            expected_result = test_case['expected_result']
            
            # 执行登录操作
            self.login.login(self.wd, user_name, user_password, screenshot_num)
            
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
    # 直接运行时执行所有测试用例
    pytest.main(['-v', __file__])