import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_excel("C:/Users/卢俊杰/Desktop/项目/项目1/中央机关及其直属机构2023年度考试录用公务员面试人员名单.xlsx")

duplicated_data = data[data.duplicated(subset=["招考职位"], keep=False)]

print("重复数据：\n", duplicated_data)

data.drop_duplicates(subset=["招考职位"], keep="first", inplace=True)

# 打印处理后的数据
print("处理后的数据：\n", data)

data["最低面试分数"] = data["最低面试分数"].astype(int)

print("处理后的数据类型：\n", data.dtypes)

data.to_excel("C:/Users/卢俊杰/Desktop/项目/项目1/clean_data.xlsx", index=False)

sample_data = data.sample(n=10, random_state=1)

print("采样后的数据：\n", sample_data)

train_data, test_data = train_test_split(data, test_size=0.2, random_state=1)

print("训练集：\n", train_data)
print("测试集：\n", test_data)
