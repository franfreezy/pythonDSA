#nyc_weather.csv contains new york city weather for first few days in the month of January. 
# Write a program that can answer following,
#What was the temperature on Jan 9?
#What was the temperature on Jan 4?
#Figure out data structure that is best for this problem
import pandas as pd

class Hashtable:
    def __init__(self) -> None:
        self.my_dict=None
        
    def dfToDict(self,DataFile):
        df=pd.read_csv(datafile)
        df=df.rename(columns={'temperature(F)':'temp'})
        self.my_dict=dict(zip(df["date"],df["temp"]))
        return (self.my_dict)
    
    def getValue(self):
        key1=input('Enter the date for which you need the data: ')
        for key2,value in self.my_dict.items(): #the items takes care of both keys and values thus 
                                                #returns both key and value
            
            if key1==key2:
                print(key2,value) 
                


if __name__=='__main__':
    item=Hashtable()
    datafile="nyc_weather.csv"
    item.dfToDict(datafile)
    item.getValue()
    