import pandas as pd

# 读取Excel文件
df = pd.read_excel('data.xlsx')

# 打印数据
print(df)

# 筛选出Sales列大于100的行
filtered_df = df[df['Sales'] > 100]

# 打印筛选结果
print("\n筛选结果（Sales > 100）:")
print(filtered_df)
