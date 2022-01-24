import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# heatmap
# `가정 및 예측`

# 나이가 어리면 a클래스가 많을 것이다
# 체지방률이 낮을수록 운동 수치가 좋을 것이다.
# 키가 클수록 앉아서 앞으로 구부리기는 잘 못할 것이다
# 혈압이 높을 수록 운동 수행능력이 떨어질 것이다
# 키가 작을 수록 멀리 뛰기는 못할 것이다.
# 몸무게가 많이 나갈 수록 악력은 쎌것이다.
# 체지방이 많을 수록 sit-ups는 못할 것이다.
# 나이, 성별, 키, 몸무게, 체지방, 혈압 중 운동 능력에 가장 많이 개입하는 것은?
# 클래스가 높게 나오려면, 어떤 수치가 가장 영향을 미치는가?

# `그래프`
# 나이에 따른 분포
# 남, 여 비율 (키, 몸무게, 체지방율 등)
# 클래스별 운동수행능력 그래프

bp = pd.read_csv("bodyPerformance.csv", header="infer")

selectdata = pd.DataFrame(bp, columns=["age", "class"])
print("select data console")
print(selectdata)

min_age = min(selectdata.loc[:, 'age'])
max_age = max(selectdata.loc[:, 'age'])

age_class_dic = {}
for i in range(len(selectdata)):
  selected_age = int(selectdata.loc[i, 'age'])

  if selectdata.loc[i, 'class'] == 'A' and selected_age not in age_class_dic.keys():
    age_class_dic[selected_age] = 1
  elif selectdata.loc[i, 'class'] == 'A' and selected_age in age_class_dic.keys():
    age_class_dic[selected_age] += 1

age_class_dic = sorted(age_class_dic.items())
x, y = zip(*age_class_dic)

plt.bar(np.arange(len(x)), y)
plt.xticks(np.arange(len(x)), x)
plt.show()

gender = bp.loc[:, 'gender']
gender.plot()
plt.show()


selectdata = bp.loc[:, ['height_cm', 'sit and bend forward_cm']]
selectdata = selectdata.sort_values('height_cm')

t = selectdata.plot()
t.set_xlabel('height_cm')
t.set_ylabel('sit and bend forward_cm')
plt.show()
