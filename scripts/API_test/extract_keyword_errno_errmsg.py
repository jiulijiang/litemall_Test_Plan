import os
import re
import csv

# 文件路径设置
md_file_path = "d:\\Gtihub\\litemall_Test_Plan\\litemall_Test_Plan\\测试用文档\\测试用例\\API\\接口测试用例_商品搜索模块.md"
output_dir = "d:\\Gtihub\\litemall_Test_Plan\\litemall_Test_Plan\\date\\ApiFox\\SearchGoods"
output_csv_path = os.path.join(output_dir, "keyword_errno_errmsg.csv")

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

# 查找表格开始的位置
start_index = -1
for i, line in enumerate(content):
    if '| ID  | 模块         | 用例名称                |' in line:
        start_index = i + 2  # 跳过表头和分隔线
        break

# 如果找到了表格开始位置，则提取数据
if start_index != -1:
    for line in content[start_index:]:
        if '|' in line and len(line.strip()) > 0:
            # 分割表格行
            parts = [p.strip() for p in line.split('|')[1:-1]]  # 移除首尾的空字符串
            
            if len(parts) >= 12:  # 确保有足够的列
                id = parts[0]
                request_url = parts[6]
                expected_data = parts[12]
                
                # 提取keyword参数
                keyword_match = re.search(r'keyword=([^&]+)', request_url)
                keyword = keyword_match.group(1) if keyword_match else ''
                
                # 提取errno
                errno_match = re.search(r'errno=([^，,]+)', expected_data)
                if errno_match:
                    errno = errno_match.group(1)
                else:
                    # 处理errno!=0的情况
                    if 'errno!=0' in expected_data:
                        errno = '!=0'
                    else:
                        errno = ''
                
                # 提取errmsg
                errmsg_match = re.search(r'errmsg="([^"]+)"', expected_data)
                errmsg = errmsg_match.group(1) if errmsg_match else ''
                
                # 只添加有keyword的行
                if keyword:
                    extracted_data.append([id, keyword, errno, errmsg])

# 写入CSV文件
if extracted_data:
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入表头
        writer.writerow(['ID', '关键词', 'errno', 'errmsg'])
        # 写入数据
        writer.writerows(extracted_data)
    
    print(f"CSV文件已成功生成到: {output_csv_path}")
    print(f"共提取了 {len(extracted_data)} 条记录")
else:
    print("未提取到数据")