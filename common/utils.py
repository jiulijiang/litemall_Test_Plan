# 导包
import json
import os
import sys
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def common_assert(response, status_code=200, errno=0, errmsg="成功"):
    # 断言响应状态码为200
    assert response.status_code == status_code
    # 断言响应数据中errno值为0
    assert response.json().get("errno") == errno
    # 断言响应数据中errmsg值为成功
    assert errmsg in response.text


# 读取JSON文件
def read_json_file(file_path):
    """读取JSON格式的测试数据文件"""
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
            
        test_data2 = []
        with open(file_path, "r", encoding="utf-8") as f:
            # 读取JSON文件
            test_data = json.load(f)
            # 将列表嵌套字典转换为列表嵌套元组
            for i in test_data:
                test_data2.append(tuple(i.values()))
        return test_data2
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return []
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return []


# 读取CSV文件
def read_csv_file(file_path):
    """读取CSV格式的测试数据文件"""
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
            
        test_data2 = []
        with open(file_path, "r", encoding="utf-8", newline='') as f:
            # 使用csv读取器读取文件
            reader = csv.DictReader(f)
            # 将每行数据转换为元组
            for row in reader:
                # 确保顺序一致
                values = [row[field] for field in reader.fieldnames]
                test_data2.append(tuple(values))
        return test_data2
    except csv.Error as e:
        print(f"CSV解析错误: {e}")
        return []
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return []


if __name__ == '__main__':
    # 获取当前文件所在目录的父目录（项目根目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 构建绝对路径
    csv_file_path = os.path.join(project_root, "date", "Api", "address_management.csv")
    test_data = read_csv_file(csv_file_path)
    print(test_data)
