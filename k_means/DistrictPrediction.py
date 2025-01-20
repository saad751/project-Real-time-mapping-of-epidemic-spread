import numpy as np
import pandas as pd
import random
import math
from sklearn.metrics import silhouette_score as shs
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('new_clustering.csv')
riverdic = {'Ganges':[ 'Mandsaur', 'Ujjain', 'Shajapur', 'Rajgarh', 'Neemuch', 'Vidisha', 'Guna', 'Shivpuri', 'Datia', 'Gwalior', 'Morena', 'Sheopur', 'Bhind', 'Tikamgarh', 'Chhattarpur', 'Panna', 'Satna', 'Rewa', 'Ashoknagar', 'Shahdol', 'Sidhi', 'Annuppur', 'Umaria', 'Katni', 'Jabalpur','Mandla', 'Dindori', 'Dhar', 'Ratlam', 'Indore', 'Dewas', 'Sehore', 'Raisen', 'Sagar', 'Bhopal', 'Damoh'],'Narmada':['Katni','Jabalpur','Damoh','Narsimhapur','Raisen','Hoshangabad','Sehore','Dewas','Dhar','Alirajpur'],'Tapi':['Betul','Burhanpur'],'Mahi':['Alirajpur'], 'Betwa':['Vidisha','Tilkamgarh','Chhatarpur','Sagar','Bhopal','Raisen'], 'Ken':['Katni','Panna','Damoh'], 'Chambal':['Mandsaur','Ratlam','Rajgarh','Ujjain','Neemuch','Shajapur','Sheopur','Shivpuri','Guna','Indore','Raisen'], 'Son':['Sidhi','Umaria','Shahdol'], 'Tons':['Rewa','Satna'], 'Sindh':['Morena','Bhind','Gwalior','Datia'], 'Wainganga':['Balaghat','Chhindwara']}
for i in range(0,50):
    data.iloc[i,2] = data.iloc[i,2][:-1]
    data.iloc[i,2] = float(data.iloc[i,2])
acc = 0.2
columns = data.columns
dic = {}
for i in columns:
    if i!='District Name':
        maxi = data[i].max()
        mini = data[i].min()
        dic[i] = (maxi,mini)
def cluster(data, nCluster, val):
    kmeans = KMeans(n_clusters=nCluster, max_iter=50, algorithm = 'auto')
    kmeans.fit(data.iloc[:, 1:])
    X = data
    l = np.zeros(nCluster)
    dict = {}
    dict1 = {}
    for i in range(len(X)):
        predict_me = np.array(X.iloc[i, 1:].astype(float))
        predict_me = predict_me.reshape(-1, len(predict_me))
        prediction = kmeans.predict(predict_me)
        l[int(prediction)]+=1
        if int(prediction) not in dict:
            dict[int(prediction)] = []
        dict[int(prediction)].append(i)
        k = 'cluster ' + str(prediction)
        if k not in dict1.keys():
            dict1[k] = []
        dict1[k].append(data.iloc[i][0])
    dict
    labels = np.zeros(len(data))

    for key, value in dict.items():
        for curidx in value:
            labels[curidx] = key

    val += shs(data.iloc[:, 1:], labels) 
    return val,dict1
  Population = 10**-1
Population_Growth = 1
Temperature_Max = 0.5 
Temperature_Min = 1
Rainfall = 2
Latitude = 0.65
Longitude = 0.19
AQI = 10.12

theta = [Population, Population_Growth, Temperature_Max, Temperature_Min, Rainfall, Latitude, Longitude, AQI]
data_new = data.iloc[:, 1:] * theta
accuracy,clusters = cluster(data, 9, acc)
print(accuracy)
clusters
# clusters.values()

list_final = []
for i in clusters.keys():
    list_final.append(clusters[i])
import pickle
with open("final_list.txt", "wb") as fp:
    pickle.dump(list_final, fp)
