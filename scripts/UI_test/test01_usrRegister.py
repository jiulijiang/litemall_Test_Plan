import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from UI.wd_init import WD_init
from UI.Mod01_usrRegister import UserRegister
from common.utils import read_json_as_dict
from common.dbutil import DBUtil

class TestUserRegister:
    """
    用户注册模块测试类
    """
    
    def setup_method(self):
        """
        用例执行前初始化webdriver对象和注册类
        """
        # 初始化浏览器
        self.wd = WD_init()
        # 初始化注册类
        self.register = UserRegister()
    
    def teardown_method(self):
        """
        用例执行完后关闭webdriver对象
        """
        # 关闭浏览器
        if hasattr(self, 'wd') and self.wd:
            self.wd.close()
    
    @pytest.mark.parametrize('test_case', read_json_as_dict('date/UI/register_cases.json'))
    def test_user_register(self, test_case):
        """
        用户注册模块参数化测试
        每个用例作为字典参数传递，在函数内部提取所需字段
        """
        try:
            # 在函数内部提取测试数据
            case_id = test_case['case_id']
            case_title = test_case['case_title']
            user_phone = test_case['user_phone']
            code = test_case['code']
            user_name = test_case['user_name']
            user_password = test_case['user_password']
            re_password = test_case.get('re_password', user_password)  # 获取确认密码，如果不存在则使用密码
            screenshot_num = test_case['screenshot_num']
            expected_result = test_case.get('expected_result', '')
            
            # 判断是否为非注册手机号
            if user_phone != "13666666666":
                # 非用于测试已注册用例，从数据库删除已存在数据
                delete_sql = f"delete from litemall.litemall_user where mobile = '{user_phone}'"
                # 创建数据库对象
                db_util = DBUtil()
                db_util.exe_sql(delete_sql)


            # 执行注册操作 - 传入所有必需参数
            self.register.register(self.wd, user_phone, code, user_name, user_password, re_password, screenshot_num,case_title)
            

            # 截图以便后期检查页面上是否显示了预期的提示信息
            print(f"测试用例{case_id}({case_title})执行完成，截图已保存")
            print(f"预期结果: {expected_result}")
            

            # 断言预期结果列表中是否有任意一个字符串包含在页面源代码中
            assert any(result in self.wd.page_source for result in expected_result), \
                f"测试用例{case_id}({case_title})失败，预期结果列表中的任何字符串都未在页面中找到: {expected_result}"


        except Exception as e:
            # 确保case_id和case_title在异常处理中可用
            case_id = test_case.get('case_id', 'Unknown')
            case_title = test_case.get('case_title', 'Unknown')
            print(f"测试用例{case_id}({case_title})执行失败: {str(e)}")
            raise

if __name__ == "__main__":
    # 直接运行时执行所有测试用例
    pytest.main(['-v', __file__])