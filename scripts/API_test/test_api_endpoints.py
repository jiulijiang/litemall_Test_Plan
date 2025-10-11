import requests
import json

# 直接定义配置信息
BASE_URL_API = "http://www.litemall360.com:8080"

# 测试登录接口
def test_login():
    url = f"{BASE_URL_API}/wx/auth/login"
    headers = {"Content-Type": "application/json"}
    body = {"username": "user123", "password": "user123"}
    response = requests.post(url=url, headers=headers, json=body)
    print(f"登录接口 - 状态码: {response.status_code}")
    print(f"登录接口 - 响应内容: {response.text}")
    try:
        return response.json().get("data", {}).get("token")
    except:
        return None

# 测试退出登录接口
def test_logout(token=None):
    url = f"{BASE_URL_API}/wx/auth/logout"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["X-Litemall-Token"] = token
    response = requests.post(url=url, headers=headers, json={})
    print(f"退出登录接口 - 状态码: {response.status_code}")
    print(f"退出登录接口 - 响应内容: {response.text}")

# 测试获取用户信息接口
def test_user_info(token=None):
    url = f"{BASE_URL_API}/wx/user/info"
    headers = {}
    if token:
        headers["X-Litemall-Token"] = token
    response = requests.get(url=url, headers=headers)
    print(f"获取用户信息接口 - 状态码: {response.status_code}")
    print(f"获取用户信息接口 - 响应内容: {response.text}")

# 测试刷新Token接口
def test_refresh_token(token=None):
    url = f"{BASE_URL_API}/wx/auth/refresh"
    headers = {}
    if token:
        headers["X-Litemall-Token"] = token
    response = requests.get(url=url, headers=headers)
    print(f"刷新Token接口 - 状态码: {response.status_code}")
    print(f"刷新Token接口 - 响应内容: {response.text}")

if __name__ == "__main__":
    print("测试API接口...")
    # 先测试未登录状态下的接口
    print("\n未登录状态:")
    test_logout()
    test_user_info()
    test_refresh_token()
    
    # 测试登录后获取token
    print("\n登录获取token:")
    token = test_login()
    print(f"获取到的token: {token}")
    
    # 如果获取到了token，测试已登录状态下的接口
    if token:
        print("\n已登录状态:")
        test_logout(token)
        test_user_info(token)
        test_refresh_token(token)