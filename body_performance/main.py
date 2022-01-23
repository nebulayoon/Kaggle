import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

# heatmap

# x = np.arange(3)
# print(x)
# years = ['2018', '2019', '2020']
# values = [100, 400, 900]

# plt.bar(x, values)
# plt.xticks(x, years)

# plt.show()

f = open('bodyPerformance.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)



count = 0
for line in rdr:
  print(line)
  count += 1
  if count == 10:
    break

bp = pd.read_csv("bodyPerformance.csv", header="infer")

selectdata = pd.DataFrame(bp, columns=["age", "class"])
print("select data console")
print(selectdata)

# for column_name, item in selectdata.iteritems():
#   print(column_name)
#   print(item[0])

min_age = min(selectdata.loc[:, 'age'])
max_age = max(selectdata.loc[:, 'age'])

dic = {}
for i in range(len(selectdata)):
  selected_age = int(selectdata.loc[i, 'age'])

  if selectdata.loc[i, 'class'] == 'A' and selected_age not in dic.keys():
    dic[selected_age] = 1
  elif selectdata.loc[i, 'class'] == 'A' and selected_age in dic.keys():
    dic[selected_age] += 1

dic = sorted(dic.items())
print(dic)
