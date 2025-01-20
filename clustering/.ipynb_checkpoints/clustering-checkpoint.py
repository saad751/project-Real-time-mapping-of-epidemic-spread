import fastai
import pandas as pd
data = pd.read_csv('data.csv')
dic = {}
for i in columns:
    if i!='States' and i!='Rivers':
        maxi = data[i].max()
        mini = data[i].min()
        dic[i] = (maxi,mini)


for i in range(0,29):
    for j in range(0,12):
        if j!=0 and j!=5 and j!=8:
            data.iloc[i,j] = (data.iloc[i,j]-dic[columns[j]][1])/(dic[columns[j]][0]-dic[columns[j]][1])
for i in range(0,29):
    data.iloc[i,8] = (data.iloc[i,8]-dic[columns[8]][1])/(dic[columns[8]][0]-dic[columns[8]][1])
def distancefunc(i,j,data):
#     print(i,j)
    dist = 0
    for k in range(0,12):
#         print(k)
        if k!=0 and k!=5:
            dist = dist + abs(data.iloc[i][k]-data.iloc[j][k])
    match = 0
    a = data.iloc[i][5].split(', ')
    b = data.iloc[j][5].split(', ')
    for river in a:
        if river in b:
            match = match + 5
    if match == 0:
        dist += 5
    else:
        dist += 1/match
    return dist
list1 = []
for i in range(0,29):
    list1.append([i])  
while (len(list1)>5):
    
    x=0
    j=0
    mini=1000
    a=[]
    b=[]
    for k in range(0,29):
        for l in range(0,29):
            for m in list1:
                if k in m:
                    a = m
            for n in list1:
                if l in n:
                    b = n
            if (k!=l) and a!=b and distancefunc(k,l,data)<mini:
                mini = distancefunc(k,l,data)
                i = k
                j = l
    c = []
    d = []
    for m in list1:
        if i in m:
            c = m
    for n in list1:
        if j in n:
            d = n
    list1.remove(c)
    list1.remove(d)
    list1.append(c+d)
list_final = []
for i in list1:
    l = []
    for j in i:
        l.append(data.iloc[j][0])
    list_final.append(l)

list_final
