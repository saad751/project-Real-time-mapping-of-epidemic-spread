import pandas as pd
df = pd.read_csv('deaths_and_cases.csv')
df.head()
columns = df.columns
columns
modic = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
       'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for index,rows in df.iterrows():
    print(rows['State'])
    break
states = []
month = []
deaths = []
cases = []
dicfac = [6/223,4/223,2/223,2/223,4/223,8/223,19/223,49/223,92/223,21/223,9/223,7/223]
for index,rows in df.iterrows():
    for i in range(0,12):
        states.append(rows['State'])
        month.append(modic[i])
        if modic[i]!='Dec':
            deaths.append(rows[modic[i]])
        else:
            deaths.append(int(rows[modic[i-1]]*dicfac[i]/dicfac[i-1]))
        cases.append(int(rows['Deaths']*dicfac[i]))

l = []
for i in range(0,420):
    l1 = []
    l1.append(states[i])
    l1.append(month[i])
    l1.append(deaths[i])
    l1.append(cases[i])
    l.append(l1)
a = [['state','Months','deaths','cases']]
l = a + l 
l
  
