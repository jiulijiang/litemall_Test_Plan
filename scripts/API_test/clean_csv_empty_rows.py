import os
import csv

# 文件路径设置
csv_file_path = "d:\Gtihub\litemall_Test_Plan\litemall_Test_Plan\date\ApiFox\Order\submit_order_params.csv"

# 读取CSV文件并过滤空行
data = []
try:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # 读取表头
        header = next(reader)
        data.append(header)
        
        # 过滤非空行
        for row in reader:
            # 检查行是否全为空
            if any(cell.strip() for cell in row):
                data.append(row)
    
    # 重写CSV文件
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"已成功清除CSV文件中的空数据行: {csv_file_path}")
    print(f"处理后共有 {len(data)} 行数据")
except Exception as e:
    print(f"处理CSV文件时出错: {e}")