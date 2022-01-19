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

bp = pd.read_csv("bodyPerformance.csv")

selectdata = pd.DataFrame(bp, columns=["gender", "systolic"])

print(selectdata)
