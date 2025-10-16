import os
import sys
import pytest

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from UI.Mod03_goodsSearch import GoodsSearch
from UI.wd_init import WD_init
from common.utils import read_json_as_dict


class TestGoodsSearch:
    """商品搜索模块测试类"""


    def setup_method(self):
        """每个测试方法执行前的初始化方法"""
        # 初始化WebDriver
        self.wd = WD_init()
        # 实例化商品搜索类
        self.search = GoodsSearch()

    def teardown_method(self):
        """每个测试方法执行后的清理方法"""
        # 关闭浏览器
        if self.wd:
            self.wd.quit()


    @pytest.mark.parametrize('test_case',read_json_as_dict('date/UI/search_cases.json') )
    def test_goods_search(self, test_case):
        """商品搜索测试方法"""
        
        try:
            case_id = test_case['case_id']
            case_title = test_case['case_title']
            keyword = test_case['keyword']
            screenshot_num = test_case['screenshot_num']
            expected_result = test_case['expected_result']
            
            # 执行搜索操作
            self.search.search(self.wd, keyword, screenshot_num)

            # 截图以便后期检查页面上是否显示了预期的提示信息
            print(f"测试用例{case_id}({case_title})执行完成，截图已保存")
            print(f"预期结果: {expected_result}")

            # 断言预期结果列表中是否有任意一个字符串包含在页面源代码中
            assert any(result in self.wd.page_source for result in expected_result), \
                f"测试用例{case_id}({case_title})失败，预期结果列表中的任何字符串都未在页面中找到: {expected_result}"
        except Exception as e:
            print(f"{case_id} - {case_title}: 测试失败，错误信息: {str(e)}")
            raise


if __name__ == "__main__":
    # 直接运行时执行pytest
    pytest.main(["-v", "test03_goodsSearch.py"])