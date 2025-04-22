import pandas as pd

# 读取Excel文件
df = pd.read_excel('data.xlsx')

# 打印前5行
print("前5行数据:")
print(df.head())

# 打印DataFrame信息概览
print("\nDataFrame信息概览:")
df.info()

# 检查'Cost'列是否有缺失值
print("\n'Cost'列缺失值数量:")
print(df['Cost'].isna().sum())

# 使用0填充'Cost'列中的缺失值
df['Cost'] = df['Cost'].fillna(0)

# 再次打印DataFrame信息以确认'Cost'列没有缺失值
print("\n填充后的DataFrame信息:")
df.info()

# 记录删除重复行前的形状
print("\n删除重复行前的DataFrame形状:")
print(df.shape)

# 删除所有完全重复的行
df = df.drop_duplicates()

# 打印删除重复行后的形状
print("\n删除重复行后的DataFrame形状:")
print(df.shape)

# 修改列名
df = df.rename(columns={'ProductName': '商品名称', 'Category': '类别'})

# 打印列名，确认修改成功
print("\n修改列名后的列名列表:")
print(df.columns)

# 新增'Profit'列，计算利润
df['Profit'] = df['Sales'] - df['Cost']

# 打印前5行，查看新增的'Profit'列
print("\n增加'Profit'列后的前5行数据:")
print(df.head())

# 按'类别'列分组并计算聚合结果
grouped_data = df.groupby('类别').agg({
    'Sales': 'sum',
    'Profit': 'mean'
})

# 打印聚合结果
print("\n按类别分组的聚合结果:")
print(grouped_data)

# 将处理好的数据保存为Excel文件，不包含索引列
df.to_excel('processed_data.xlsx', index=False)

print("\n数据已保存至 'processed_data.xlsx'")
