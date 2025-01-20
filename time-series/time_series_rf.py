%load_ext autoreload
%autoreload 2

%matplotlib inline

  from fastai.imports import *
from fastai.structured import *

from pandas_summary import DataFrameSummary
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from IPython.display import display

from sklearn import metrics
df_raw = pd.read_csv(f'{path}time-series.csv', low_memory=False)
columns = df_raw.columns
columns
dic = {}
for i in columns:
    if i!='District Name':
        #maxi = df_raw[i].max()
        mini = df_raw[i].min()
        dic[i] = mini
dic
l = [['month', 'year', 'state', 'Deaths', ' Cases', 'so2', 'no2', 'rspm/pm',
       'precipitation', 'population density',
       ' Number of Rural Hospitals (Govt.)',
       'Number of Urban Hospitals (Govt.)', 'Birth Rate', '% with toilets',
       'Humidity', 'Average temp']]
l1 = []
l10 = {}
l5 = [['month', 'year', 'state', 'Deaths', ' Cases', 'so2', 'no2', 'rspm/pm',
       'precipitation', 'population density',
       ' Number of Rural Hospitals (Govt.)',
       'Number of Urban Hospitals (Govt.)', 'Birth Rate', '% with toilets',
       'Humidity', 'Average temp']]
l6 = [['month', 'year', 'state', 'Deaths', ' Cases', 'so2', 'no2', 'rspm/pm',
       'precipitation', 'population density',
       ' Number of Rural Hospitals (Govt.)',
       'Number of Urban Hospitals (Govt.)', 'Birth Rate', '% with toilets',
       'Humidity', 'Average temp']]

for i in range(0,360):
    if True:
        if df_raw.iloc[i][0] == 'Mar':
            l10[df_raw.iloc[i][2]]=df_raw.iloc[i][4]
        
        l2 = [] 
        l2.append(df_raw.iloc[i][0])
        l2.append(2015)
        l2.append(df_raw.iloc[i][2])
        l2.append(df_raw.iloc[i][3])
        l2.append(df_raw.iloc[i][4])
        l2.append(df_raw.iloc[i][5])
        l2.append(df_raw.iloc[i][6])
        l2.append(df_raw.iloc[i][7])
        l2.append(df_raw.iloc[i][8])
        l2.append(df_raw.iloc[i][9])
        l2.append(df_raw.iloc[i][10])
        l2.append(df_raw.iloc[i][11])
        l2.append(df_raw.iloc[i][12])
        l2.append(df_raw.iloc[i][13])
        l2.append(df_raw.iloc[i][14])
        l2.append(df_raw.iloc[i][15])
        l5.append(l2)
        l3 = []
        l3.append(df_raw.iloc[i][0])
        l3.append(2016)
        l3.append(df_raw.iloc[i][2])
        l3.append(df_raw.iloc[i][3]+dic[columns[3]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][4]+dic[columns[4]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][5]+dic[columns[5]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][6]+dic[columns[6]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][7]+dic[columns[7]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][8]+dic[columns[8]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][9]+dic[columns[9]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][10]+dic[columns[10]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][11]+dic[columns[11]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][12]+dic[columns[12]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][13]+dic[columns[13]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][14]+dic[columns[14]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][15]+dic[columns[15]]*random.uniform(0, 1))
        l6.append(l3)   
        l1.append(l3)
    else:
        l2 = [] 
        l2.append(df_raw.iloc[i][0])
        l2.append(2015)
        l2.append(df_raw.iloc[i][2])
        l2.append(df_raw.iloc[i][3])
        l2.append(df_raw.iloc[i][4])
        l2.append(df_raw.iloc[i][5])
        l2.append(df_raw.iloc[i][6])
        l2.append(df_raw.iloc[i][7])
        l2.append(df_raw.iloc[i][8])
        l2.append(df_raw.iloc[i][9])
        l2.append(df_raw.iloc[i][10])
        l2.append(df_raw.iloc[i][11])
        l2.append(df_raw.iloc[i][12])
        l2.append(df_raw.iloc[i][13])
        l2.append(df_raw.iloc[i][14])
        l2.append(df_raw.iloc[i][15])
        l.append(l2)
        l3 = []
        l3.append(df_raw.iloc[i][0])
        l3.append(2016)
        l3.append(df_raw.iloc[i][2])
        l3.append(df_raw.iloc[i][3]+dic[columns[3]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][4]+dic[columns[4]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][5]+dic[columns[5]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][6]+dic[columns[6]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][7]+dic[columns[7]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][8]+dic[columns[8]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][9]+dic[columns[9]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][10]+dic[columns[10]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][11]+dic[columns[11]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][12]+dic[columns[12]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][13]+dic[columns[13]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][14]+dic[columns[14]]*random.uniform(0, 1))
        l3.append(df_raw.iloc[i][15]+dic[columns[15]]*random.uniform(0, 1))
        l1.append(l3)
a = pd.DataFrame(l5+l1)
a.to_csv('train_2015_2016.csv',index=False,header=False)
b = pd.DataFrame(l6)
b.to_csv('test_2015_2016.csv',index=False,header=False)
df_train = pd.read_csv(f'{path}train_2015_2016.csv', low_memory=False)
df_test = pd.read_csv(f'{path}test_2015_2016.csv', low_memory=False)
train_cats(df_train)
train_cats(df_test)
x_train, y_train, nas = proc_df(df_train, ' Cases')
x_test, y_test,nas = proc_df(df_test,' Cases',na_dict=nas)
m = RandomForestRegressor(n_estimators = 10,n_jobs=-1,max_depth = 6,max_features=0.5)
m.fit(x_train, y_train)
print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
train_cats(df_raw)
df,y,nas = proc_df(df_raw,' Cases',na_dict=nas)
fi = rf_feat_importance(m, df)
# plt.plot(fi)
print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
l10
