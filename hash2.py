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
        print(self.my_dict)


if __name__=='__main__':
    item=Hashtable()
    datafile="nyc_weather.csv"
    item.dfToDict(datafile)
    