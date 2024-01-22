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
        data.loc[-1] = data.columns.values
        data.sort_index(inplace=True)
        data.reset_index(drop=True, inplace=True)
        data=data.rename(columns={'Two roads diverged in a yellow wood,':'dta'})
       
        for row in data.iterrows():
            row=data['dta'].to_list()
            
        print(row)   
        
    def ArrangeData(self):
        pass
        
        
if __name__=='__main__':
    item=hashtable()
    datafile="poem.txt"
    item.GetData(datafile)