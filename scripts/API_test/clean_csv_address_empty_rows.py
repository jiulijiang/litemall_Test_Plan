import os
import csv

# 文件路径设置
csv_file_path = r"d:\Gtihub\litemall_Test_Plan\litemall_Test_Plan\date\ApiFox\Address\add_address_params.csv"

# 检查文件是否存在
if not os.path.exists(csv_file_path):
    print(f"文件不存在: {csv_file_path}")
    exit(1)

# 读取CSV文件并过滤空行
try:
    # 存储非空行数据
    non_empty_rows = []
    
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # 保留表头
        header = next(reader)
        non_empty_rows.append(header)
        
        # 过滤空行
        for row in reader:
            # 检查行是否包含非空值
            if any(cell.strip() != '' for cell in row):
                non_empty_rows.append(row)
    
    # 重写CSV文件，移除空行
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(non_empty_rows)
    
    print(f"成功清除CSV文件中的空数据行: {csv_file_path}")
    print(f"处理后文件包含 {len(non_empty_rows)} 行数据")

except Exception as e:
    print(f"清理CSV文件空行时出错: {e}")