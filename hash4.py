#Implement hash table where collisions are handled using linear probing.
#  We learnt about linear probing in the video tutorial. 
# Take the hash table implementation that uses chaining and 
# modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.
#a hash table
import pandas as pd
#employing OOP
class hashTable:
    def __init__(self) -> None:
        self.max_value=100
        self.arr=[None for i in range(self.max_value)]

    def processCsv(self,DataFile):
        self.df=pd.read_csv(DataFile)
        self.df=self.df.rename(columns={'date':'Date','temperature(F)':'temp'})
        return self.df

    def dataFrameToArray(self, df):
        myArray=[]
        for index,row in df.iterrows():
            date = row['Date']
            temp = row['temp']
            data=date,temp
            myArray.append(data)
        return myArray