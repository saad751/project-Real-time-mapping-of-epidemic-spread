import numpy as np
import pandas as pd
import torch.nn as nn
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
from torch.utils.data import DataLoader, Dataset
import torchvision
from torchvision import transforms
import pandas_profiling
from sklearn.model_selection import train_test_split, ParameterGrid
import parfit.parfit as pf
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv("finalData.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
df.head()
def bool_to_int(x):
    if x:
        return 1
    return 0    
df['Labels'] = df['Labels'].apply(bool_to_int)
df.head()
df.to_csv("final_data.csv")
data_profile = pandas_profiling.ProfileReport(df)
data_profile.to_file(outputfile = "data_profile.html")
!firefox data_profile.html

X, y = df.drop("Labels", axis = 1), df.Labels
X_train, X_test, y_train, y_test = train_test_split(X, y)

df_train, df_test = train_test_split(df)
df_train.to_csv("final_data_train.csv")
df_test.to_csv("final_data_test.csv")
class Load_data(Dataset):
    
    def __init__(self, file_path, transform=None):
        self.data = pd.read_csv(file_path)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        X = self.data.iloc[index, 2:]
        label = self.data.iloc[index, 1]
        return torch.Tensor(X.values), label
      train_dataset = Load_data("final_data_train.csv", transform=None)
test_dataset = Load_data("final_data_test.csv", transform=None)
all_loader = Load_data("final_data.csv", transform=None)

train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=8, shuffle=True)
all_loader = DataLoader(test_dataset, batch_size=8, shuffle=True)
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(348, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net().cuda()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(10000):  
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        # get the inputs
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs.cuda())
        loss = criterion(outputs, labels.cuda())
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2 == 0:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Finished Training')


