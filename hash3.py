#poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in python and print every word and its count as show below.
#  Think about the best data structure that you can use to solve this problem and
#  figure out why you selected that specific data structure.
# 'diverged': 2,
 #'in': 3,
# 'I': 8

import pandas as pd

class hashtable:
    def __init__(self) -> None:
        self.my_dict=None

    def GetData(self,datafile):
        data=pd.read_fwf(datafile)
        for row in data:
            print(row)
       
    def ArrangeData(self):
        pass
        
        
if __name__=='__main__':
    item=hashtable()
    datafile="poem.txt"
    item.GetData(datafile)