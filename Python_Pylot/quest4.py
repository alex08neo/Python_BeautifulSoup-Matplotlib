import csv, pprint
import pandas as pd
import matplotlib.pyplot as plt


#by using pandas to change csv to dictonary
state_contractor=[]
stateList1 =[]
contractorList = []
stateContractorSoredList = []
quest4FirstSateList = []
quest4FirstContractorList = []

state_operator =[]
stateList2 = []
operatorList = []
stateOperatorSoredList = []
quest4SecondSateList = []
quest4SecondOperatorList = []

data = pd.read_csv("Wells.06.03.18Rigs.CSV")
data_dic = {col:list(data[col]) for col in data.columns}


state_contractor = list(zip(data_dic['State/Province'],data_dic['Contractor Name'] ))
state_operator = list(zip(data_dic['State/Province'],data_dic['Operator Name'] ))

for i in state_contractor:
    if i[0] not in stateList1:
        stateList1.append(i[0])

newDic2 = dict((m, []) for m in stateList1)

for i in state_contractor:
        if i[0] in newDic2.keys():
             newDic2[i[0]].append(i[1])

for i in newDic2.values():
      contractorList.append(len(list(set(i))))

stateContractorSoredList=sorted(dict(zip(stateList1,contractorList)).items(), key=lambda d:d[1], reverse=True)
# print(stateContractorSoredList)
for i in range(0,5):
    quest4FirstSateList.append(stateContractorSoredList[i][0])
    quest4FirstContractorList.append((stateContractorSoredList[i][1]))
print (quest4FirstSateList)
# output: ['Texas', 'New Mexico', 'Oklahoma', 'Louisiana', 'Gulf of Mexico']
print (quest4FirstContractorList)
# output: [65, 22, 18, 17, 15]

print("-----------------------------------------")


for i in state_operator:
    if i[0] not in stateList2:
        stateList2.append(i[0])

newDic2 = dict((m, []) for m in stateList2)

for i in state_operator:
        if i[0] in newDic2.keys():
             newDic2[i[0]].append(i[1])

for i in newDic2.values():
      operatorList.append(len(list(set(i))))

stateOperatorSoredList=sorted(dict(zip(stateList2,operatorList)).items(), key=lambda d:d[1], reverse=True)
# print(stateContractorSoredList)
for i in range(0,5):
    quest4SecondSateList.append(stateOperatorSoredList[i][0])
    quest4SecondOperatorList.append((stateOperatorSoredList[i][1]))

print (quest4SecondSateList)
# output ['Texas', 'Oklahoma', 'New Mexico', 'Louisiana', 'North Dakota']
print (quest4SecondOperatorList)
# output [216, 67, 39, 29, 26]

#from output of the above code I can create four new arries
arry1x=['TX', 'NM', 'OK', 'LA', 'Gulf']
arry1y=[65, 22, 18, 17, 15]

arry2x=['TX', 'OK', 'NM', 'LA', 'ND']
arry2y=[216, 67, 39, 29, 26]

# plt.figure = (1, figsize=(10,5))
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.xlabel('Top 5 Regions')
plt.ylabel('Number of Contractor')
plt.bar(arry1x,arry1y, color='r', label='Contractor')
plt.legend()

plt.subplot(122)
plt.xlabel('Top 5 Regions')
plt.ylabel('Number of Operator')
plt.bar(arry2x,arry2y, color='y', label='Operator')
plt.legend()

plt.show()

