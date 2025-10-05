import sys
import os
import requests
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class OrderAPI:
    # 1.搜索
    def login(self,userName= config.USER_NAME,passWord= config.USER_PASSWORD):
        url = config.BASE_URL + "/wx/auth/login"
        json_login = {"username": userName, "password": passWord}
        header_login = {"Content-Type": "application/json"}
        response = requests.post(url,
                                 headers=header_login, # 这里不写也可，可以直接传json
                                 json=json_login)
        return response
    # 2.搜索
    def search(self,keyword):
        url = config.BASE_URL + f"/wx/goods/list?keyword={keyword}&page=1&limit=10&categoryId=0"
        response = requests.get(url)
        return response
    # 3.加入购物车
    def add_to_cart(self,token,goodsId):
        url = config.BASE_URL + f"/wx/cart/add"
        header_cart = {"X-Litemall-Token": token}
        json_cart = {"goodsId":goodsId,"number":5,"productId":2} 
        response = requests.post(url,headers=header_cart,json=json_cart)
        return response
    # 4.提交订单
    def submit_order(self,token):
        url = config.BASE_URL + f"/wx/order/submit"
        header_order = {"X-Litemall-Token": token,"Content-Type": "application/json"}
        json_order = {"addressId":"1","cartId":"0","couponId":"0","userCouponId":"0","grouponLinkId":0,"grouponRulesId":0,"message":""} 
        response = requests.post(url,headers=header_order,json=json_order)
        return response
    # 5.查询订单详情
    def query_order_detail(self,token):
        url = config.BASE_URL + f"/wx/order/list?showType=0&page=1&limit=10"
        header_order = {"X-Litemall-Token": token}
        response = requests.get(url,headers=header_order)
        return response



# 冒烟测试
if __name__ == "__main__":
    order_api = OrderAPI()
    response = order_api.login()
    token = response.json().get("data").get("token")
    goodsId = order_api.search(keyword="母亲节").json().get("data").get("list")[0].get("id")
    response = order_api.add_to_cart(token=token,goodsId=goodsId)
    response = order_api.submit_order(token=token)
    response = order_api.query_order_detail(token=token)
    try:
        errmsg = response_data.get("errmsg", "")
        # 检查errmsg是否包含"成功"
        assert errmsg is not None and "成功" in errmsg
        print("所有动作成功")
    except AssertionError:
        print(f"查询订单详情失败，响应消息: {errmsg if 'errmsg' in locals() else '无消息'}")
        raise
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"响应解析错误: {str(e)}")
        print(f"原始响应内容: {response.text}")
        raise
