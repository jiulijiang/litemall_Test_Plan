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

    def addToCart(self,GOODS_ID: str,GOODS_NUM: str,productId = "2",tokenCart = None):
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

if __name__ == "__main__":
    test = LiteMallAPI()
    print(test.getCartGoodsNum().json())