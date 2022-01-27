import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] =  15
matplotlib.rcParams['axes.unicode_minus'] = False
import seaborn as sns
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

# plt.switch_backend('Agg') # back-end server의 matplotlib을 비대화형 서버로 변환(non-interactive)

bp = pd.read_csv("bodyPerformance.csv", header="infer")

ax = sns.heatmap(bp)
plt.show()

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

plt.figure(figsize=(10, 5))
plt.bar(np.arange(len(x)), y)
plt.xticks(np.arange(len(x)), x)
plt.show()

# 전체 사용자의 세대 별 몇명인지 표시
tw = selectdata.loc[(selectdata['age'] >= 20) & (selectdata['age'] < 30)]
th = selectdata.loc[(selectdata['age'] >= 30) & (selectdata['age'] < 40)]
fr = selectdata.loc[(selectdata['age'] >= 40) & (selectdata['age'] < 50)]
etc = selectdata.loc[(selectdata['age'] >= 50)]

pie_generation_values = np.array([tw.count()[0], th.count()[0], fr.count()[0], etc.count()[0]])
pie_generation_labels = ['20G', '30G', '40G', '50G over']

print(pie_generation_values)
print(type(tw.count()[0]))
wedgeprops = { 'width':0.6, 'edgecolor':'w', 'linewidth':5 }
plt.pie(pie_generation_values, labels=pie_generation_labels, autopct='%.2f%%', startangle=90, wedgeprops=wedgeprops, pctdistance=0.7, counterclock=False)
plt.legend()
plt.show()

# 각 세대별 A클래스의 비율

tw_aclass = selectdata.loc[(selectdata['age'] >= 20) & (selectdata['age'] < 30) & (selectdata['class'] == 'A')].count()[0]
th_aclass = selectdata.loc[(selectdata['age'] >= 30) & (selectdata['age'] < 40) & (selectdata['class'] == 'A')].count()[0]
fr_aclass = selectdata.loc[(selectdata['age'] >= 40) & (selectdata['age'] < 50) & (selectdata['class'] == 'A')].count()[0]
etc_aclass = selectdata.loc[(selectdata['age'] >= 50) & (selectdata['class'] == 'A')].count()[0]

aclass_num = np.array([tw_aclass, th_aclass, fr_aclass, etc_aclass])
aclass_num = aclass_num / pie_generation_values * 100
print(aclass_num.sum())
print(aclass_num)
plt.plot( pie_generation_labels, aclass_num, marker='o')
plt.title('각 세대별 aclass 비율')
plt.show()
  



# from flask import Flask
# #from flask import render_template
# import io
# import base64

# app = Flask(__name__)

# @app.route('/plot')
# def build_plot():

#     img = io.BytesIO()

#     y = [1,2,3,4,5]
#     x = [0,2,1,3,4]
#     plt.plot(x,y)
#     plt.savefig(img, format='png')
#     img.seek(0)

#     plot_url = base64.b64encode(img.getvalue()).decode()

#     return '<img src="data:image/png;base64,{}">'.format(plot_url)

# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='192.168.0.2', port='5000')

# gender = bp.loc[:, 'gender']
# gender.plot()
# plt.show()


# selectdata = bp.loc[:, ['height_cm', 'sit and bend forward_cm']]
# selectdata = selectdata.sort_values('height_cm')

# t = selectdata.plot()
# t.set_xlabel('height_cm')
# t.set_ylabel('sit and bend forward_cm')
# plt.show()
