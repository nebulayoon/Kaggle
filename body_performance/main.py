import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)
print(x)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)

plt.show()