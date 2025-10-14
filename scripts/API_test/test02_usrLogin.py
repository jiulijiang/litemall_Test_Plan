import os
import sys
import pytest

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 导入必要的模块
from api.Litemall_API import LiteMallAPI
from common.utils import read_json_file, common_assert

class TestUserLogin:
    """
    测试用户登录接口
    """

    def setup_method(self):
        """
        初始化API方法实例
        """
        self.api = LiteMallAPI()

    @pytest.mark.parametrize("id,name,username,password,expected_status_code,expected_errno,expected_errmsg_patterns"
        , read_json_file("date/Api/login_cases.json"))
    def test_login(self, id, name, username, password, expected_status_code, expected_errno, expected_errmsg_patterns):
        """
        测试用户登录接口
        """
        # 打印测试用例信息
        print(f"\n测试用例 {id}: {name}")
        print(f"用户名: {username}")
        print(f"密码: {password}")
        print(f"预期: status_code={expected_status_code}, errno={expected_errno}, errmsg_patterns={expected_errmsg_patterns}")
        # 调用登录接口
        resp = self.api.usrLogin(USER_NAME=username, USER_PASSWORD=password)
        # 打印实际响应信息
        print(f"实际: status_code={resp.status_code}")
        print(f"响应内容: {resp.text}")
        # 解析JSON响应
        json_response = resp.json()
        # 打印响应信息
        print(f"JSON响应: {json_response}")
        print(f"实际errno: {json_response.get('errno')}")
        print(f"实际errmsg: {json_response.get('errmsg')}")
        # 断言响应状态码和内容
        common_assert(resp, status_code=expected_status_code, errno=expected_errno, errmsg=expected_errmsg_patterns)
