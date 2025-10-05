# 导包
import json


def common_assert(response, status_code=200, errno=0, errmsg="成功"):
    # 断言响应状态码为200
    assert response.status_code == status_code
    # 断言响应数据中errno值为0
    assert response.json().get("errno") == errno
    # 断言响应数据中errmsg值为成功
    assert errmsg in response.text


def read_json_file(fileName):
    test_data2 = []
    with open(fileName, "r", encoding="utf-8") as f:
        # 读取文件
        test_data = json.load(f)
        # 需求：列表嵌套字典转换为列表嵌套元组
        # [{}, {}, {}] → [(), (), ()]
        # 分析：
        # 1、获取字典values值 dict.values()
        # 2、将values值转换为元组 tuple(values)
        # 3、将元组数据追加到列表中 list.append()
        for i in test_data:
            test_data2.append(tuple(i.values()))
    return test_data2


if __name__ == '__main__':
    test_data = read_json_file("../data/login.json")
    print(test_data)
