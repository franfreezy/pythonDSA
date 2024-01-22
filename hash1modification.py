# i think hashmaps are basically dicts in python and therefore we don't need to
#make an array with hash as index but its a good way to show how hash tables work

import pandas as pd
#employing OOP
class hashTable:
    def __init__(self) -> None:
        self.my_dict={}

    def processCsv(self,DataFile):
        self.df=pd.read_csv(DataFile)
        self.df=self.df.rename(columns={'date':'Date','temperature(F)':'temp'})
        result_dict=dict(zip(self.df["Date"],self.df["temp"]))
        self.my_dict=result_dict
        return self.my_dict

if __name__=='__main__':
    item=hashTable()
    dataFile="nyc_weather.csv"
    print(item.processCsv(dataFile))