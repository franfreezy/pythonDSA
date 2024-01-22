# i think hashmaps are basically dicts in python and therefore we don't need to
#make an array with hash as index but its a good way to show how hash tables work

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
