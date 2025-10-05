import os
import sys
import utils
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from api.api_order import OrderAPI

class TestOrderAPI:
    # 类前置方法
    def setup_class(self):
        # 实例化接口类
        self.order_api = OrderAPI()



    def test01_login(self):
        # 调用登录接口
        response = self.order_api.login()
        # 提取token
        self.token = response.json().get("data").get("token")
        # 断言登录成功
        try:
            errmsg = response.json().get("errmsg", "")
            assert errmsg is not None and "成功" in errmsg
            print("登录成功")
        except AssertionError:
            print("登录失败")
            raise

    def test02_search(self):
        # 调用查询订单接口
        response = self.order_api.search(keyword="母亲节")
        # 提取商品id
        self.goodsId = response.json().get("data").get("list")[0].get("id")
        # 断言查询成功
        try:
            errmsg = response.json().get("errmsg", "")
            assert errmsg is not None and "成功" in errmsg
            print("查询订单成功")
        except AssertionError:
            print("查询订单失败")
            raise

    def test03_add_to_cart(self):
        #登录获取token
        self.test01_login()
        #搜索获取商品id
        self.test02_search()
        # 调用添加到购物车接口
        response = self.order_api.add_to_cart(token = self.token,goodsId = self.goodsId)
        # 断言添加成功
        try:
            errmsg = response.json().get("errmsg", "")
            assert errmsg is not None and "成功" in errmsg
            print("添加到购物车成功")
        except AssertionError:
            print("添加到购物车失败")
            raise
    def test03_submit(self):
        #登录获取token
        self.test01_login()
        # 调用提交订单接口
        response = self.order_api.submit_order(token = self.token)
        # 断言提交成功
        try:
            errmsg = response.json().get("errmsg", "")
            assert errmsg is not None and "成功" in errmsg
            print("提交订单成功")
        except AssertionError:
            print("提交订单失败")
            raise

    def test04_detail(self):
        #登录获取token
        self.test01_login()
        # 调用查询订单详情接口
        response = self.order_api.query_order_detail(token = self.token)
        # 断言查询成功
        try:
            errmsg = response.json().get("errmsg", "")
            assert errmsg is not None and "成功" in errmsg
            print("查询订单详情成功")
        except AssertionError:
            print("查询订单详情失败")
            raise
