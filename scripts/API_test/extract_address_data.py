import os
import re
import csv
import json

# 文件路径设置
md_file_path = "d:\Gtihub\litemall_Test_Plan\litemall_Test_Plan\测试用文档\测试用例\API\接口测试用例_地址管理模块.md"
output_dir = "d:\Gtihub\litemall_Test_Plan\litemall_Test_Plan\date\ApiFox\Address"
output_csv_path = os.path.join(output_dir, "add_address_params.csv")

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取Markdown文件内容
try:
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
except Exception as e:
    print(f"读取文件失败: {e}")
    exit(1)

# 提取数据
extracted_data = []

# 查找添加地址接口测试用例表格
start_processing = False
for i, line in enumerate(content):
    # 标记添加地址接口测试用例表格的开始
    if '### 1.1 添加地址接口测试用例' in line:
        # 跳过表头和分隔线
        header_line = i + 3  # 第i+1行是表格标题，i+2行是表头，i+3行是分隔线
        start_processing = True
        continue
    # 标记下一个测试用例表格的开始，停止处理
    elif start_processing and '### 1.' in line and not '### 1.1' in line:
        break
    
    # 处理表格内容
    if start_processing and '|' in line and len(line.strip()) > 0:
        # 分割表格行
        parts = [p.strip() for p in line.split('|')[1:-1]]  # 移除首尾的空字符串
        
        if len(parts) >= 12:  # 确保有足够的列（包含预期返回数据列）
            case_id = parts[0]
            
            # 获取请求参数列
            request_params = parts[10]
            # 获取预期返回数据列（应该是第12列，索引为12）
            expected_data = parts[12] if len(parts) > 12 else ''
            
            # 初始化变量
            name = ''
            tel = ''
            country = ''
            province = ''
            city = ''
            county = ''
            area_code = ''
            postal_code = ''
            address_detail = ''
            is_default = ''
            errno = ''
            errmsg = ''
            
            # 解析JSON格式的请求参数
            try:
                # 处理可能的转义字符和格式问题
                # 移除可能的反斜杠转义
                request_params = request_params.replace('\\', '')
                # 确保是有效的JSON格式
                if '{' in request_params and '}' in request_params:
                    # 处理可能包含的<br>标签和换行
                    request_params = re.sub(r'<br>', ' ', request_params)
                    request_params = re.sub(r'\n', ' ', request_params)
                    json_str = re.search(r'\{.*\}', request_params).group(0)
                    params = json.loads(json_str)
                    
                    # 提取需要的字段
                    name = params.get('name', '')
                    tel = params.get('tel', '')
                    country = params.get('country', '')
                    province = params.get('province', '')
                    city = params.get('city', '')
                    county = params.get('county', '')
                    area_code = params.get('areaCode', '')
                    postal_code = params.get('postalCode', '')
                    address_detail = params.get('addressDetail', '')
                    is_default = params.get('isDefault', '')
            except Exception as e:
                print(f"解析请求参数失败 (ID: {case_id}): {e}")
                # 继续处理，即使请求参数解析失败，也尝试提取errno和errmsg
            
            # 解析预期返回数据，提取errno和errmsg
            try:
                # 打印原始数据用于调试
                print(f"原始预期数据 (ID: {case_id}): {expected_data}")
                
                # 处理可能的转义字符和格式问题
                expected_data = expected_data.replace('\\', '')
                # 移除HTML标签和换行符
                expected_data = re.sub(r'<[^>]+>', '', expected_data)
                expected_data = expected_data.replace('\n', '').replace('\r', '')
                
                # 打印处理后的数据
                print(f"处理后的数据: {expected_data}")
                
                # 使用更灵活的正则表达式直接提取errno和errmsg
                # 提取errno - 支持数字和占位符格式，考虑JSON格式中的引号
                errno_match = re.search(r'"errno"\s*:\s*([^,}]+)', expected_data)
                if errno_match:
                    errno_value = errno_match.group(1).strip('"[] ')
                    if '非' in errno_value:
                        errno = '非0'
                    else:
                        errno = errno_value
                else:
                    errno = ''
                
                # 提取errmsg - 尝试更宽松的匹配模式
                errmsg_match = re.search(r'errmsg[:=]\s*"([^"]+)"', expected_data)
                if not errmsg_match:
                    # 尝试其他可能的格式
                    errmsg_match = re.search(r'"errmsg"\s*:\s*"([^"]+)"', expected_data)
                if not errmsg_match:
                    # 尝试最宽松的匹配
                    errmsg_match = re.search(r'errmsg.*?([^,\}]+)', expected_data)
                
                if errmsg_match:
                    errmsg = errmsg_match.group(1).strip('"')
                else:
                    errmsg = ''
                
            except Exception as e:
                print(f"解析预期返回数据失败 (ID: {case_id}): {e}")
                errno = ''
                errmsg = ''
            
            # 打印提取结果用于调试
            print(f"提取结果 (ID: {case_id}): errno={errno}, errmsg={errmsg}")
            
            # 添加到提取的数据列表
            extracted_data.append([name, tel, country, province, city, county, area_code, postal_code, address_detail, is_default, errno, errmsg])

# 写入CSV文件
if extracted_data:
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入表头，包含所有需要的字段
        writer.writerow(['name', 'tel', 'country', 'province', 'city', 'county', 'areaCode', 'postalCode', 'addressDetail', 'isDefault', 'errno', 'errmsg'])
        # 写入数据
        writer.writerows(extracted_data)
    
    print(f"CSV文件已成功生成到: {output_csv_path}")