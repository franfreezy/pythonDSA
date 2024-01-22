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
        return self.my_dict.values()
    
    def get_highest(self):
        values=self.my_dict.values() #values in my dict
        max_value=max(values) #computes the max in the values. py in built fn
        return max_value #prints it
    
    def get_average(self):
        count=0
        sum=0
        days=int(input('Enter the number of days to compute average: '))
        for value in self.my_dict.values():
            if count<days:
                sum=sum+value
                print(count+1)
                count+=1
        average=sum/days
        return average
            
    

if __name__=='__main__':
    item=hashTable()
    dataFile="nyc_weather.csv"
    print(item.processCsv(dataFile))
    print(item.get_highest())
    print(item.get_average())