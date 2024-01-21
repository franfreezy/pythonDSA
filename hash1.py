#nyc_weather.csv contains new york city weather for first few days in the month of
# January. 
#Write a program that can answer following,
#What was the average temperature in first week of Jan
#What was the maximum temperature in first 10 days of Jan
#Figure out data structure that is best for this problem

import pandas as pd


df=pd.read_csv(r"nyc_weather.csv")

def dataFrameToArray(df):
    myArray=[]
    for row in df:
        myArray.append(row)
    return myArray
# we can now use hash maps
print(df)
print(dataFrameToArray(df))


#we can now create a class to take care of the hash table stuffs
class hashTable:
    def __init__(self) -> None:
        self.max_value=10
        self.arr=[None for i in range(self.max_value)]
    
    #this is the hash function, converts the key to an index for the table
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char) #this ord() function converts the char to ascii value
            return h%self.max_value
    


     
if __name__=='__main__':
    item=hashTable()






