import os
import sys
import os
import pytest

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 导入必要的模块
from api.Litemall_API import LiteMallAPI
from common.utils import read_json_file, common_assert
from common.dbutil import DBUtil

class TestUserRegister:
    """
    测试用户注册接口
    """

    def setup_method(self):
        """
        初始化API方法实例
        """
        self.api = LiteMallAPI()

    def __getMsg(self, mobile):
        """
        用于短信正常情况下获取短信验证码
        """
        resp = self.api.getverifyCode(USER_PHONE=mobile)
        return resp.json().get("data", {}).get("verify_code")



    @pytest.mark.parametrize("id,name,mobile,expected_status_code,expected_errno,expected_errmsg_patterns"
        , read_json_file("date/Api/sms_captcha_cases.json"))
    def test_register_msg(self, id, name, mobile, expected_status_code, expected_errno, expected_errmsg_patterns):
        """
        认证模块测试-测试短信验证码接口
        """
        # 打印测试用例信息
        print(f"\n测试用例 {id}: {name}")
        print(f"手机号: {mobile}")
        print(f"预期: status_code={expected_status_code}, errno={expected_errno}, errmsg_patterns={expected_errmsg_patterns}")
        # 调用短信验证码接口
        resp = self.api.getverifyCode(USER_PHONE=mobile)
        # 打印实际响应信息
        print(f"实际: status_code={resp.status_code}")
        print(f"响应内容: {resp.text}")
        try:
            json_response = resp.json()
            print(f"JSON响应: {json_response}")
            print(f"实际errno: {json_response.get('errno')}")
            print(f"实际errmsg: {json_response.get('errmsg')}")
        except Exception as e:
            print(f"解析JSON失败: {e}")
        # 断言响应状态码
        common_assert(resp, status_code=expected_status_code, errno=expected_errno, errmsg=expected_errmsg_patterns)




    @pytest.mark.parametrize(
        "id,name,code,username,password,mobile,expected_status_code,expected_errno,expected_errmsg_patterns,check_data"
        , read_json_file("date/Api/register_cases.json"))
    def test_register(self, id, name, code, username, password, mobile, expected_status_code, expected_errno,
                      expected_errmsg_patterns, check_data):
        """
        认证模块测试-测试用户注册接口
        """
        # 检查手机号是否已注册,已注册则从数据库删除对应数据
        check_sql = f"select  * from litemall.litemall_user where mobile = '{mobile}'"
        print(f"执行SQL查询: {check_sql}")
        result = DBUtil.exe_sql(check_sql)
        
        # 检查结果是否有效
        print(f"查询结果: {result}")
        if result is not None and len(result) > 0 and result[0][0] > 0:
            # 手机号已注册,删除对应数据
            delete_sql = f"delete from litemall.litemall_user where mobile = '{mobile}'"
            DBUtil.exe_sql(delete_sql)
            print(f"已删除手机号为 {mobile} 的用户数据")
        elif result is None:
            print("警告: 数据库操作失败，跳过数据清理步骤")
        else:
            print(f"手机号 {mobile} 未注册，无需清理数据")



        # 打印测试用例信息
        print(f"\n测试用例 {id}: {name}")
        print(f"手机号: {mobile}")
        print(f"用户名: {username}")
        print(f"密码: {password}")
        print(f"验证码: {code}")
        print(f"预期: status_code={expected_status_code}, errno={expected_errno}, errmsg_patterns={expected_errmsg_patterns}")
        # 调用注册接口 
        self.__getMsg(mobile)  # 获取短信验证码
        resp = self.api.usrRigister(USER_CODE=code,USER_NAME=username,USER_PASSWORD=password,USER_PHONE=mobile)
        # 打印实际响应信息
        print(f"实际: status_code={resp.status_code}")
        print(f"响应内容: {resp.text}")
        try:
            json_response = resp.json()
            print(f"JSON响应: {json_response}")
        except Exception as e:
            print(f"解析JSON失败: {e}")
        # 断言响应状态码
        common_assert(resp, status_code=expected_status_code, errno=expected_errno, errmsg=expected_errmsg_patterns)
        
