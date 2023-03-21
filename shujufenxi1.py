import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/卢俊杰/Desktop/项目/项目1/clean_data1.xlsx")

bins = [0, 60, 80, 100, 120, 140, 160]
labels = ["0-60", "60-80", "80-100", "100-120", "120-140", "140-160"]
data["分数区间"] = pd.cut(data["最低面试分数"], bins=bins, labels=labels)

plt.hist(data["分数区间"], bins=labels)

plt.title("最低面试分数分布")
plt.xlabel("分数区间")
plt.ylabel("人数")

plt.show()
