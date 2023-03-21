import pandas as pd

data = pd.read_excel("C:/Users/卢俊杰/Desktop/项目/项目1/clean_data.xlsx")
data.sort_values(by="最低面试分数", inplace=True)
data.to_excel("C:/Users/卢俊杰/Desktop/项目/项目1/clean_data1.xlsx", index=False)
