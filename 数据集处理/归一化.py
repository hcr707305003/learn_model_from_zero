import pandas as pd
import numpy as np

# 假设我们有一个简单的数据集
data = pd.DataFrame({
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [28, np.nan, 35, 32],
    'gender': ['M', 'F', 'M', np.nan]
})

# 处理缺失值，这里我们选择用平均值填充年龄，众数填充性别
data['age'] = data['age'].fillna(data['age'].mean())
data['gender'] = data['gender'].fillna(data['gender'].mode()[0])

# 数据转换，将性别的M和F转为0和1
data['gender'] = data['gender'].map({'M': 0, 'F': 1})

# 获取原始数据中的最小值和最大值
min_age = data['age'].min()
max_age = data['age'].max()

# 数据归一化（公式：年龄 - 最小年龄 / 最大年龄 - 最小年龄）, 将年龄规范到0-1之间
data['age'] = (data['age'] - min_age) / (max_age - min_age)

# 获取原来的数值
data['source_age'] = data['age'] * (max_age - min_age) + min_age

print(data)