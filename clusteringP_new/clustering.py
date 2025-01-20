riverdic = {'Ganges':[ 'Mandsaur', 'Ujjain', 'Shajapur', 'Rajgarh', 'Neemuch', 'Vidisha', 'Guna', 'Shivpuri', 'Datia', 'Gwalior', 'Morena', 'Sheopur', 'Bhind', 'Tikamgarh', 'Chhattarpur', 'Panna', 'Satna', 'Rewa', 'Ashoknagar', 'Shahdol', 'Sidhi', 'Annuppur', 'Umaria', 'Katni', 'Jabalpur','Mandla', 'Dindori', 'Dhar', 'Ratlam', 'Indore', 'Dewas', 'Sehore', 'Raisen', 'Sagar', 'Bhopal', 'Damoh'],'Narmada':['Katni','Jabalpur','Damoh','Narsimhapur','Raisen','Hoshangabad','Sehore','Dewas','Dhar','Alirajpur'],'Tapi':['Betul','Burhanpur'],'Mahi':['Alirajpur'], 'Betwa':['Vidisha','Tilkamgarh','Chhatarpur','Sagar','Bhopal','Raisen'], 'Ken':['Katni','Panna','Damoh'], 'Chambal':['Mandsaur','Ratlam','Rajgarh','Ujjain','Neemuch','Shajapur','Sheopur','Shivpuri','Guna','Indore','Raisen'], 'Son':['Sidhi','Umaria','Shahdol'], 'Tons':['Rewa','Satna'], 'Sindh':['Morena','Bhind','Gwalior','Datia'], 'Wainganga':['Balaghat','Chhindwara']}
riverdic_final = {}
for i in riverdic.keys():
    for j in riverdic[i]:
        if j not in riverdic_final.keys():
            riverdic_final[j] = []
            riverdic_final[j].append(i)
        else:
            riverdic_final[j].append(i)

import fastai
import pandas as pd
data = pd.read_csv('new_clustering.csv')
for i in range(0,50):
#     print(data.iloc[i][2])
    data.iloc[i,2] = data.iloc[i,2][:-1]
    data.iloc[i,2] = float(data.iloc[i,2])
columns = data.columns

dic = {}
for i in columns:
    if i!='District Name':
        maxi = data[i].max()
        mini = data[i].min()
        dic[i] = (maxi,mini)

for i in range(0,50):
    for j in range(0,9):
        if j!=0:
            
            data.iloc[i,j] = (data.iloc[i,j]-dic[columns[j]][1])/(dic[columns[j]][0]-dic[columns[j]][1])

for i in range(0,29):
    data.iloc[i,8] = (data.iloc[i,8]-dic[columns[8]][1])/(dic[columns[8]][0]-dic[columns[8]][1])
def distancefunc(i,j,data):
#     print(i,j)
    dist = 0
    for k in range(0,9):
#         print(k)
        if k!=0:
            dist = dist + abs(data.iloc[i][k]-data.iloc[j][k])
    match = 0
#     a = data.iloc[i][5].split(', ')
#     a=[]
#     if data.iloc[i][0] in riverdic_final.keys():
#         a = riverdic_final[data.iloc[i][0]]
#     b = data.iloc[j][5].split(', ')
    b = []
#     if data.iloc[j][0] in riverdic_final.keys():
#         b = riverdic_final[data.iloc[j][0]]
#     for river in a:
#         if river in b:
#             match = match + 2
#     if match == 0:
#         dist += 1
#     else:
#         dist += 1/match
    return dist

list1 = []
for i in range(0,50):
    list1.append([i])
  list1
while (len(list1)>20):
    
    x=0
    j=0
    mini=1000
    a=[]
    b=[]
    for k in range(0,50):
        for l in range(0,50):
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
