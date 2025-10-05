## 轻商城litemall

### 系统信息

- 系统路径：http://www.litemall360.com:8080


### 1、获取首页数据

#### 基本信息

- `Path：/wx/home/index`
- `Method:GET`

#### 返回数据

- 响应状态码：200

- 返回数据：

  ```yacas
  {
      "errno": 0,
      "data": {
          "newGoodsList": [
              {
                  "id": 1181000,
                  "name": "母亲节礼物-舒适安睡组合",
                  "brief": "安心舒适是最好的礼物",
                  "picUrl": "http://yanxuan.nosdn.127.net/1f67b1970ee20fd572b7202da0ff705d.png",
                  "isNew": true,
                  "isHot": false,
                  "counterPrice": 2618.00,
                  "retailPrice": 2598.00
              }
              ......
         ],
          ......
      },
      "errmsg": "成功"
  }
  ```

  



### 2、注册

#### 2.1 获取短信验证码

##### 基本信息

- `Path：/wx/auth/regCaptcha`
- `Method:POST`



##### 请求参数

**headers**

| 参数名称     | 参数值           | 是否必填 | 示例 | 备注 |
| ------------ | ---------------- | -------- | ---- | ---- |
| Content-Type | application/json |          |      |      |

**body**

| 参数名称 | 类型   | 是否必填 | 示例 | 备注   |
| -------- | ------ | -------- | ---- | ------ |
| mobile   | string | 是       |      | 手机号 |

```yacas
{"mobile":"13606150002"}
```



##### 返回数据

- 响应状态码：200

- 响应数据：

  ```yacas
  {
      "errno": 0,
      "errmsg": "成功"
  }
  ```

  

#### 2.2 注册

##### 基本信息

- `Path：/wx/auth/register`
- `Method:POST`
- 接口描述:

##### 请求参数

**headers**

| 参数名称     | 参数值           | 是否必填 | 示例 | 备注 |
| ------------ | ---------------- | -------- | ---- | ---- |
| Content-Type | application/json |          |      |      |

**body**

| 参数名称       | 类型   | 是否必填 | 示例 | 备注       |
| -------------- | ------ | -------- | ---- | ---------- |
| code           | string | 是       |      | 短信验证码 |
| username       | string | 是       |      | 用户名     |
| password       | string | 是       |      | 密码       |
| repeatPassword | string | 是       |      | 确认密码   |
| mobile         | string | 是       |      | 手机号     |

```yacas
{"code":"666666","username":"jack102","password":"123456","repeatPassword":"123456","mobile":"13606150002"}
```



##### 返回数据

- 响应状态码：200

- 响应数据

  ```yacas
  {
      "errno": 0,
      "data": {
          "userInfo": {
              "nickName": "jack102",
              "avatarUrl": "https://yanxuan.nosdn.127.net/80841d741d7fa3073e0ae27bf487339f.jpg?imageView&quality=90&thumbnail=64x64"
          },
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aGlzIGlzIGxpdGVtYWxsIHRva2VuIiwiYXVkIjoiTUlOSUFQUCIsImlzcyI6IkxJVEVNQUxMIiwiZXhwIjoxNjU2NzI1MjYzLCJ1c2VySWQiOjIsImlhdCI6MTY1NjcxODA2M30.1amm6MbkuP7txWWaRkSh1DYwq98oGZzIGriQMANF6Po"
      },
      "errmsg": "成功"
  }
  ```





### 3、登录

#### 基本信息

- `Path：/wx/auth/login`
- `Method:POST`
- 接口描述:

#### 请求参数

**headers**

| 参数名称     | 参数值           | 是否必填 | 示例 | 备注 |
| ------------ | ---------------- | -------- | ---- | ---- |
| Content-Type | application/json |          |      |      |

**body**

| 参数名称 | 类型   | 是否必填 | 示例 | 备注   |
| -------- | ------ | -------- | ---- | ------ |
| username | string | 是       |      | 用户名 |
| password | string | 是       |      | 密码   |

```yacas
{"username":"user123","password":"user123"} 
```



#### 返回数据

- 响应状态码：200

- 响应数据：

  ```yacas
  {
      "errno": 0,
      "data": {
          "userInfo": {
              "nickName": "user123",
              "avatarUrl": ""
          },
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aGlzIGlzIGxpdGVtYWxsIHRva2VuIiwiYXVkIjoiTUlOSUFQUCIsImlzcyI6IkxJVEVNQUxMIiwiZXhwIjoxNjU2NzI1NjA3LCJ1c2VySWQiOjEsImlhdCI6MTY1NjcxODQwN30.56h8c53HNk_KYSGS07kIo5O234AT0bezVtkriRY5Q4Y"
      },
      "errmsg": "成功"
  }
  ```
  
  

### 4、搜索

#### 基本信息

- `Path：/wx/goods/list?keyword=母亲节&page=1&limit=10&categoryId=0`
- `Method:GET`

#### 返回数据

- 响应状态码：200

- 响应数据：

  ```yacas
  {
      "errno": 0,
      "data": {
          "total": 1,
          "pages": 1,
          "limit": 10,
          "page": 1,
          "list": [
              {
                  "id": 1181000,
                  "name": "母亲节礼物-舒适安睡组合",
                  "brief": "安心舒适是最好的礼物",
                  "picUrl": "http://yanxuan.nosdn.127.net/1f67b1970ee20fd572b7202da0ff705d.png",
                  "isNew": true,
                  "isHot": false,
                  "counterPrice": 2618.00,
                  "retailPrice": 2598.00
              }
          ],
          "filterCategoryList": [
              {
                  "id": 1008008,
                  "name": "被枕",
                  "keywords": "",
                  "desc": "守护你的睡眠时光",
                  "pid": 1005000,
                  "iconUrl": "http://yanxuan.nosdn.127.net/927bc33f7ae2895dd6c11cf91f5e3228.png",
                  "picUrl": "http://yanxuan.nosdn.127.net/b43ef7cececebe6292d2f7f590522e05.png",
                  "level": "L2",
                  "sortOrder": 2,
                  "addTime": "2018-02-01 00:00:00",
                  "updateTime": "2018-02-01 00:00:00",
                  "deleted": false
              }
          ]
      },
      "errmsg": "成功"
  }
  ```
  
  

### 5、获取商品信息

#### 基本信息

- `Path：/wx/goods/detail?id=1181000`
- `Method:GET`
- 接口描述: id为商品id

#### 返回数据

- 响应状态码：200

- 响应数据

  ```yacas
  {
      "errno": 0,
      "data": {
          "specificationList": [
              {
                  "name": "规格",
                  "valueList": [
                      {
                          "id": 1,
                          "goodsId": 1181000,
                          "specification": "规格",
                          "value": "1.5m床垫*1+枕头*2",
                          "picUrl": "",
                          "addTime": "2018-02-01 00:00:00",
                          "updateTime": "2018-02-01 00:00:00",
                          "deleted": false
                      },
                      {
                          "id": 2,
                          "goodsId": 1181000,
                          "specification": "规格",
                          "value": "1.8m床垫*1+枕头*2",
                          "picUrl": "",
                          "addTime": "2018-02-01 00:00:00",
                          "updateTime": "2018-02-01 00:00:00",
                          "deleted": false
                      }
                  ]
              },
              ......
      },
      "errmsg": "成功"
  }
  ```
  
  
  
  

### 6、获取购物车商品数量

#### 基本信息

- `Path：/wx/cart/goodscount`
- `Method:GET`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值 | 是否必填 | 示例 | 备注            |
| ---------------- | ------ | -------- | ---- | --------------- |
| X-Litemall-Token |        | 是       |      | 登录成功Token值 |


#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {"errno":0,"data":0,"errmsg":"成功"}
  ```



### 7、加入购物车

#### 基本信息

- `Path：/wx/cart/add`
- `Method:POST`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值           | 是否必填 | 示例 | 备注            |
| ---------------- | ---------------- | -------- | ---- | --------------- |
| X-Litemall-Token |                  | 是       |      | 登录成功Token值 |
| Content-Type     | application/json |          |      |                 |

**body**

| 参数名称  | 类型 | 是否必填 | 示例 | 备注     |
| --------- | ---- | -------- | ---- | -------- |
| goodsId   | int  | 是       |      | 商品id   |
| number    | int  | 是       |      | 购买数量 |
| productId | int  | 是       |      | 产品id   |

```yacas
{"goodsId":1181000,"number":5,"productId":2} 
```



#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {"errno":0,"data":5,"errmsg":"成功"}
  ```



### 8、查看购物车

#### 基本信息

- `Path：/wx/cart/index`
- `Method:GET`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值 | 是否必填 | 示例 | 备注            |
| ---------------- | ------ | -------- | ---- | --------------- |
| X-Litemall-Token |        | 是       |      | 登录成功Token值 |


#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {
      "errno": 0,
      "data": {
          "cartTotal": {
              "goodsCount": 5,
              "checkedGoodsCount": 5,
              "goodsAmount": 7500.00,
              "checkedGoodsAmount": 7500.00
          },
          "cartList": [
              {
                  "id": 1,
                  "userId": 1,
                  "goodsId": 1181000,
                  "goodsSn": "1181000",
                  "goodsName": "母亲节礼物-舒适安睡组合",
                  "productId": 2,
                  "price": 1500.00,
                  "number": 5,
                  "specifications": [
                      "1.5m床垫*1+枕头*2",
                      "玛瑙红"
                  ],
                  "checked": true,
                  "picUrl": "quality=90&thumbnail=200x200&imageView",
                  "addTime": "2022-07-02 07:46:45",
                  "updateTime": "2022-07-02 07:46:45",
                  "deleted": false
              }
          ]
      },
      "errmsg": "成功"
  }
  ```



### 9、选中商品

#### 基本信息

- `Path：/wx/cart/checked`
- `Method:POST`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值           | 是否必填 | 示例 | 备注            |
| ---------------- | ---------------- | -------- | ---- | --------------- |
| X-Litemall-Token |                  | 是       |      | 登录成功Token值 |
| Content-Type     | application/json |          |      |                 |

**body**

| 参数名称   | 类型 | 是否必填 | 示例 | 备注                |
| ---------- | ---- | -------- | ---- | ------------------- |
| productIds | list | 是       |      | 产品id              |
| isChecked  | int  | 是       |      | 选中状态：1表示选中 |

```yacas
{"productIds":[232,31],"isChecked":1}
```



#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {
      "errno": 0,
      "data": {
          "cartTotal": {
              "goodsCount": 5,
              "checkedGoodsCount": 5,
              "goodsAmount": 7500.00,
              "checkedGoodsAmount": 7500.00
          },
          "cartList": [
              {
                  "id": 1,
                  "userId": 1,
                  "goodsId": 1181000,
                  "goodsSn": "1181000",
                  "goodsName": "母亲节礼物-舒适安睡组合",
                  "productId": 2,
                  "price": 1500.00,
                  "number": 5,
                  "specifications": [
                      "1.5m床垫*1+枕头*2",
                      "玛瑙红"
                  ],
                  "checked": true,
                  "picUrl": "quality=90&thumbnail=200x200&imageView",
                  "addTime": "2022-07-02 07:46:45",
                  "updateTime": "2022-07-02 07:46:45",
                  "deleted": false
              }
          ]
      },
      "errmsg": "成功"
  }
  ```



### 10、结算商品

#### 基本信息

- `Path：/wx/cart/checkout?cartId=0&addressId=0&couponId=0&userCouponId=0&grouponRulesId=0`
- `Method:GET`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值 | 是否必填 | 示例 | 备注            |
| ---------------- | ------ | -------- | ---- | --------------- |
| X-Litemall-Token |        | 是       |      | 登录成功Token值 |

#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {
      "errno": 0,
      "data": {
          "grouponRulesId": 0,
          "actualPrice": 7500.00,
          "orderTotalPrice": 7500.00,
          "cartId": 0,
          "userCouponId": 0,
          "couponId": 0,
          "goodsTotalPrice": 7500.00,
          "addressId": 0,
          "grouponPrice": 0,
          "checkedAddress": {
              "id": 0
          },
          "couponPrice": 0,
          "availableCouponLength": 0,
          "freightPrice": 0,
          "checkedGoodsList": [
              {
                  "id": 1,
                  "userId": 1,
                  "goodsId": 1181000,
                  "goodsSn": "1181000",
                  "goodsName": "母亲节礼物-舒适安睡组合",
                  "productId": 2,
                  "price": 1500.00,
                  "number": 5,
                  "specifications": [
                      "1.5m床垫*1+枕头*2",
                      "玛瑙红"
                  ],
                  "checked": true,
                  "picUrl": "quality=90&thumbnail=200x200&imageView",
                  "addTime": "2022-07-02 07:46:45",
                  "updateTime": "2022-07-02 07:46:45",
                  "deleted": false
              }
          ]
      },
      "errmsg": "成功"
  }
  ```



### 11、添加地址

#### 基本信息

- `Path：/wx/address/save`
- `Method:POST`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值           | 是否必填 | 示例 | 备注            |
| ---------------- | ---------------- | -------- | ---- | --------------- |
| X-Litemall-Token |                  | 是       |      | 登录成功Token值 |
| Content-Type     | application/json |          |      |                 |

**body**

| 参数名称      | 类型    | 是否必填 | 示例        | 备注     |
| ------------- | ------- | -------- | ----------- | -------- |
| name          | string  | 是       | jack001     | 姓名     |
| tel           | string  | 是       | 13611224455 | 手机号   |
| country       | string  | 是       | China       | 国家     |
| province      | string  | 是       | Beijing     | 省       |
| city          | string  | 是       | Beijing     | 市       |
| county        | string  | 是       | HaiDian     | 县       |
| areaCode      | string  | 是       | 110101      | 地区代码 |
| postalCode    | string  | 是       | 100091      | 邮政编码 |
| addressDetail | string  | 是       | heima       | 详细地址 |
| isDefault     | boolean | 是       | true        | 默认地址 |

```yacas
{"name":"jack001","tel":"13611224455","country":"China","province":"Beijing","city":"Beijing","county":"HaiDian","areaCode":"110101","postalCode":"100091","addressDetail":"heima","isDefault":true}
```



#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {"errno":0,"data":2,"errmsg":"成功"}
  ```



### 12、查看地址

#### 基本信息

- `Path：/wx/address/list`
- `Method:GET`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值 | 是否必填 | 示例 | 备注            |
| ---------------- | ------ | -------- | ---- | --------------- |
| X-Litemall-Token |        | 是       |      | 登录成功Token值 |


#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {
      "errno": 0,
      "data": {
          "total": 2,
          "pages": 1,
          "limit": 2,
          "page": 1,
          "list": [
              {
                  "id": 2,
                  "name": "jack001",
                  "userId": 1,
                  "province": "Beijing",
                  "city": "Beijing",
                  "county": "HaiDian",
                  "addressDetail": "heima",
                  "areaCode": "110101",
                  "postalCode": "100091",
                  "tel": "13611224455",
                  "isDefault": true,
                  "addTime": "2022-07-02 08:02:35",
                  "updateTime": "2022-07-02 08:02:35",
                  "deleted": false
              }
          ]
      },
      "errmsg": "成功"
  }
  ```



### 13、提交订单

#### 基本信息

- `Path：/wx/order/submit`
- `Method:POST`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值           | 是否必填 | 示例 | 备注            |
| ---------------- | ---------------- | -------- | ---- | --------------- |
| X-Litemall-Token |                  | 是       |      | 登录成功Token值 |
| Content-Type     | application/json |          |      |                 |

**body**

| 参数名称       | 类型   | 是否必填 | 示例 | 备注                         |
| -------------- | ------ | -------- | ---- | ---------------------------- |
| addressId      | String | 是       | 2    | 收货地址                     |
| cartId         | String | 是       | 0    | 购物车的信息标识符           |
| couponId       | String | 是       | 0    | 优惠券的唯一标识符           |
| userCouponId   | String | 是       | 0    | 用户与优惠券之间的唯一标识符 |
| grouponLinkId  | int    | 是       | 0    | 团购链接的唯一标识符         |
| grouponRulesId | int    | 是       | 0    | 团购规则的唯一标识符         |
| message        | String | 否       |      | 备注消息                     |

```yacas
{"addressId":"2","cartId":"0","couponId":"0","userCouponId":"0","grouponLinkId":0,"grouponRulesId":0,"message":""} 
```



#### 返回数据

- 响应状态码：200

- 响应数据：

  ```yacas
  {
      "errno": 0,
      "data": {
          "orderId": 1,
          "grouponLinkId": 0
      },
      "errmsg": "成功"
  }
  ```



### 14、查看订单

#### 基本信息

- `Path：/wx/order/list?showType=0&page=1&limit=10`
- `Method:GET`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值 | 是否必填 | 示例 | 备注            |
| ---------------- | ------ | -------- | ---- | --------------- |
| X-Litemall-Token |        | 是       |      | 登录成功Token值 |


#### 返回数据

- 响应状态码：200

- 响应数据：

  ```json
  {
      "errno": 0,
      "data": {
          "total": 1,
          "pages": 1,
          "limit": 10,
          "page": 1,
          "list": [
              {
                  "orderStatusText": "未付款",
                  "aftersaleStatus": 0,
                  "isGroupin": false,
                  "orderSn": "20220702967857",
                  "actualPrice": 7500.00,
                  "goodsList": [
                      {
                          "number": 5,
                          "picUrl": "quality=90&thumbnail=200x200&imageView",
                          "price": 1500.00,
                          "id": 1,
                          "goodsName": "母亲节礼物-舒适安睡组合",
                          "specifications": [
                              "1.5m床垫*1+枕头*2",
                              "玛瑙红"
                          ]
                      }
                  ],
                  "id": 1,
                  "handleOption": {
                      "cancel": true,
                      "delete": false,
                      "pay": true,
                      "comment": false,
                      "confirm": false,
                      "refund": false,
                      "rebuy": false,
                      "aftersale": false
                  }
              }
          ]
      },
      "errmsg": "成功"
  }
  ```



### 15、商品收藏

#### 基本信息

- `Path：/wx/collect/addordelete`
- `Method:POST`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值           | 是否必填 | 示例 | 备注            |
| ---------------- | ---------------- | -------- | ---- | --------------- |
| X-Litemall-Token |                  | 是       |      | 登录成功Token值 |
| Content-Type     | application/json |          |      |                 |

**body**

| 参数名称 | 类型   | 是否必填 | 示例 | 备注 |
| -------- | ------ | -------- | ---- | ---- |
| valueId  | String | 是       |      |      |
| type     | String | 是       |      |      |

```yacas
{"valueId":"1023034","type":0}
```



#### 返回数据

- 响应状态码：200

- 响应数据：

  ```yacas
  {"errno":0,"errmsg":"成功"}
  ```



### 16、我的收藏

#### 基本信息

- `Path：/wx/user/index`
- `Method:GET`
- 接口描述:

#### 请求参数

**headers**

| 参数名称         | 参数值 | 是否必填 | 示例 | 备注            |
| ---------------- | ------ | -------- | ---- | --------------- |
| X-Litemall-Token |        | 是       |      | 登录成功Token值 |


#### 返回数据

- 响应状态码：200

- 响应数据：

  ```yacas
  {
      "errno": 0,
      "data": {
          "order": {
              "unrecv": 0,
              "uncomment": 0,
              "unpaid": 1,
              "unship": 0
          }
      },
      "errmsg": "成功"
  }
  ```

