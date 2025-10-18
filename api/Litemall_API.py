import sys
import os
from http.client import responses

import requests
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class LiteMallAPI:
    def __getToken(self):
        """
        获取token
        """
        urlGetToken = config.BASE_URL_API+ "/wx/auth/login"
        headerGetToken = {
            "Content-Type": "application/json"
        }
        bodyGetToken = {
            "username": config.USER_NAME,
            "password": config.USER_PASSWORD
        }
        response = requests.post(url=urlGetToken, headers=headerGetToken, json=bodyGetToken)
        return response.json().get("data").get("token")

    def getHomePageData(self):
        """
        获取首页数据
        """
        urlGetData = config.BASE_URL_API+ "/wx/home/index"
        return requests.get(url = urlGetData)

    def getverifyCode(self,USER_PHONE: str):
        """
        获取验证码
        """
        urlGetVerifyCode = config.BASE_URL_API+ "/wx/auth/regCaptcha"
        headerGetVerifyCode = {
            "Content-Type": "application/json"
        }
        bodyGetVerifyCode = {
            "mobile": USER_PHONE
        }
        return requests.post(url=urlGetVerifyCode, headers=headerGetVerifyCode, json=bodyGetVerifyCode)

    def usrRigister(self,USER_CODE: str,USER_NAME: str,USER_PASSWORD: str,USER_PHONE: str):
        """
        用户注册,测试用验证码为666666
        """
        urlRegister = config.BASE_URL_API+ "/wx/auth/register"
        headerRegister = {
            "Content-Type": "application/json"
        }
        bodyRegister = {
            "code": USER_CODE,
            "username": USER_NAME,
            "password": USER_PASSWORD,
            "repeatPassword": USER_PASSWORD,
            "mobile": USER_PHONE
        }
        return requests.post(url=urlRegister, headers=headerRegister, json=bodyRegister)

    def usrLogin(self,USER_NAME: str,USER_PASSWORD: str):
        """
        用户登录
        """
        urlLogin = config.BASE_URL_API+ "/wx/auth/login"
        headerLogin = {
            "Content-Type": "application/json"
        }
        bodyLogin = {
            "username": USER_NAME,
            "password": USER_PASSWORD
        }
        return requests.post(url=urlLogin, headers=headerLogin, json=bodyLogin)

    def usrSearch(self,SEARCH_KEY: str):
        """
        用户搜索
        """
        urlSearch = config.BASE_URL_API+ f"/wx/goods/list?keyword={SEARCH_KEY}&page=1&limit=10&categoryId=0"

        return requests.get(url=urlSearch)

    def getGoodsInfo(self,GOODS_ID: str):
        """
        获取商品信息
        """
        urlGoodsInfo = config.BASE_URL_API+ f"/wx/goods/detail?id={GOODS_ID}"
        return requests.get(url=urlGoodsInfo)

    def getCartGoodsNum(self,tokenCartNum = None):
        """
        获取购物车物品数量
        """
        if tokenCartNum == None:
            tokenCartNum = self.__getToken()
        urlCartNum = config.BASE_URL_API+ "/wx/cart/goodscount"
        headerCartNum = {
            "X-Litemall-Token": tokenCartNum
        }
        return requests.get(url=urlCartNum, headers=headerCartNum)

    def addToCart(self,GOODS_ID: int,GOODS_NUM: int,productId = "2",tokenCart = None):
        """
        加入购物车
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlAddToCart = config.BASE_URL_API+ "/wx/cart/add"
        headerAddToCart = {
            "X-Litemall-Token": tokenCart,
            "Content-Type": "application/json"
        }
        bodyAddToCart = {
            "goodsId": GOODS_ID,
            "number": GOODS_NUM,
            "productId": productId
        }
        return requests.post(url=urlAddToCart, headers=headerAddToCart, json=bodyAddToCart)

    def checkCart(self,tokenCart = None):
        """
        查看购物车
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        url = config.BASE_URL_API+ "/wx/cart/index"
        headerCheckCart = {
            "X-Litemall-Token": tokenCart
        }
        return requests.get(url=url, headers=headerCheckCart)

    def selectGoodsInCart(self,ID_LIST,Checked,tokenCart = None):
        """
        选择购物车物品
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlSelectGoodsInCart = config.BASE_URL_API+ "/wx/cart/checked"
        headerSelectGoodsInCart = {
            "X-Litemall-Token": tokenCart,
            "Content-Type": "application/json"
        }
        bodySelectGoodsInCart = {
            "productIds":ID_LIST,
            "isChecked":Checked
        }
        return requests.post(url=urlSelectGoodsInCart, headers=headerSelectGoodsInCart, json=bodySelectGoodsInCart)

    def settleGoods(self,tokenCart = None):
        """
        去结算
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlSettleGoods = config.BASE_URL_API+ "/wx/cart/checkout?cartId=0&addressId=0&couponId=0&userCouponId=0&grouponRulesId=0"
        headerSettleGoods = {
            "X-Litemall-Token": tokenCart
        }
        return requests.get(url=urlSettleGoods, headers=headerSettleGoods)

    def addAddress(self,NAME: str, PHONE: str,COUNTRY: str, PROVINCE: str,
                   CITY: str, COUNTY: str, AREA_CODE: str, POSTAL_CODE: str,
                   ADDRESS_DETAIL: str, IS_DEFAULT: bool,tokenCart = None):
        """
        添加地址
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlAddAddress = config.BASE_URL_API+ "/wx/address/save"
        headerAddAddress = {
            "X-Litemall-Token": tokenCart,
            "Content-Type": "application/json"
        }
        bodyAddAddress = {
            "name":NAME,
            "tel":PHONE,
            "country":COUNTRY,
            "province":PROVINCE,
            "city":CITY,
            "county":COUNTY,
            "areaCode":AREA_CODE,
            "postalCode":POSTAL_CODE,
            "addressDetail":ADDRESS_DETAIL,
            "isDefault": IS_DEFAULT
        }
        return requests.post(url=urlAddAddress, headers=headerAddAddress, json=bodyAddAddress)

    def checkAddress(self,tokenCart = None):
        """
        查看地址
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlCheckAddress = config.BASE_URL_API+ "/wx/address/list"
        headerCheckAddress = {
            "X-Litemall-Token": tokenCart
        }
        return requests.get(url=urlCheckAddress, headers=headerCheckAddress)


    def subOder(self,ADDRESS_ID: str,CART_ID: str,COUPON_ID: str,
                USER_COUPON_ID: str,GROUPON_LINK_ID: int,
                GROUPON_RULES_ID: int,MESSAGE: str,tokenCart = None):
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlSubOder = config.BASE_URL_API+ "/wx/order/submit"
        headerSubOder = {
            "X-Litemall-Token": tokenCart,
            "Content-Type": "application/json"
        }
        bodySubOder = {
            "addressId":ADDRESS_ID,
            "cartId":CART_ID,
            "couponId":COUPON_ID,
            "userCouponId":USER_COUPON_ID,
            "grouponLinkId":GROUPON_LINK_ID,
            "grouponRulesId":GROUPON_RULES_ID,
            "message":MESSAGE
        }
        return requests.post(url=urlSubOder, headers=headerSubOder, json=bodySubOder)

    def getOrderList(self,tokenCart = None):
        """
        获取订单列表
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlOrderList = config.BASE_URL_API+ "/wx/order/list?showType=0&page=1&limit=10"
        headerOrderList = {
            "X-Litemall-Token": tokenCart
        }
        return requests.get(url=urlOrderList, headers=headerOrderList)


    def coollectGoods(self,VALUE_ID: str,TYPE: int,tokenCart = None):
        """
        收藏物品
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlCollectGoods = config.BASE_URL_API+ "/wx/collect/addordelete"
        headerCollectGoods = {
            "X-Litemall-Token": tokenCart,
            "Content-Type": "application/json"
        }
        bodyCollectGoods = {
            "valueId":VALUE_ID,
            "type":TYPE
        }
        return requests.post(url=urlCollectGoods, headers=headerCollectGoods, json=bodyCollectGoods)

    def myCollectGoods(self,tokenCart = None):
        """
        查看收藏物品
        """
        if tokenCart == None:
            tokenCart = self.__getToken()
        urlMyCollectGoods = config.BASE_URL_API+ "/wx/user/index"
        headerMyCollectGoods = {
            "X-Litemall-Token": tokenCart
        }
        return requests.get(url = urlMyCollectGoods, headers=headerMyCollectGoods)

if __name__ == "__main__":
    test = LiteMallAPI()
    
    # 批量注册测试账号-性能测试准备
    import csv
    import time
    
    # 读取CSV文件中的账号信息
    with open('Jmeter/userlogin.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过表头
        
        # 从13900000000开始的手机号序列
        phone_base = 13900000000
        
        for i, row in enumerate(reader):
            username, password = row
            phone = str(phone_base + i)
            
            # 先获取验证码
            verify_response = test.getverifyCode(phone)
            print(f"获取验证码 for {phone}: {verify_response.json()}")
            
            # 注册账号（使用固定验证码666666）
            response = test.usrRigister("666666", username, password, phone)
            print(f"注册账号 {username} ({phone}): {response.json()}")
            
            # 添加延迟避免请求过于频繁
            time.sleep(0.5)
    