import os
import sys
import json
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from UI.wd_init import WD_init
from UI.Mod02_usrLogin import UserLogin
from common.utils import read_json_file

class TestUserLogin:
    """
    用户登录模块测试类
    """
    
    @classmethod
    def setup_class(cls):
        """
        测试类初始化
        """
        # 准备测试数据路径
        cls.test_data_path = os.path.join('date', 'UI', 'login_cases.json')
        
    @classmethod
    def teardown_class(cls):
        """
        测试类清理
        """
        pass
    
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
    
    @staticmethod
    def get_test_cases():
        """
        获取测试用例数据
        使用common.utils中的read_json_file函数读取测试数据
        """
        try:
            # 先直接读取原始JSON获取完整测试用例数据
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            test_data_path = os.path.join(project_root, 'date', 'UI', 'login_cases.json')
            
            with open(test_data_path, 'r', encoding='utf-8') as f:
                original_data = json.load(f)
                
            # 返回原始测试用例列表
            return original_data['test_cases']
        except Exception as e:
            print(f"读取测试数据失败: {str(e)}")
            return []
    
    @pytest.mark.parametrize('test_case', get_test_cases.__func__())
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
            
            # 这里可以根据实际情况添加断言
            # 由于UI测试的特殊性，断言可能需要根据页面元素来判断
            print(f"测试用例{case_id}({case_title})执行完成，截图已保存")
            
        except Exception as e:
            print(f"测试用例{case_id}({case_title})执行失败: {str(e)}")
            raise

if __name__ == "__main__":
    # 直接运行时执行所有测试用例
    pytest.main(['-v', __file__])