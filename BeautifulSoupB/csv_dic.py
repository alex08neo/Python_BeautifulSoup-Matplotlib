import csv, pprint
import pandas as pd

#by using pandas to change csv to dictonary
def genRegionDicFromCsv(csvfile):
    newDic = {}
    data = pd.read_csv(csvfile)
    data_dic = {col: list(data[col]) for col in data.columns}
    return data_dic

#csv to distionary without method and printing
newDic = {}
data = pd.read_csv("Wells.06.03.18Rigs.CSV")
data_dic = {col:list(data[col]) for col in data.columns}
newDic = {'region':data_dic["OFS Region"],'rigname':data_dic["Rig Name/Number"],'state':data_dic['State/Province'],
          'operator':data_dic['Operator Name'], 'contractor':data_dic['Contractor Name'],
          'rig_lat':data_dic['Rig Latitude (WGS84)'],'rig_long':data_dic['Rig Longitude (WGS84)']}
pprint.pprint(newDic)

