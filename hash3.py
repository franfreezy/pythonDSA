#poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in python and print every word and its count as show below.
#  Think about the best data structure that you can use to solve this problem and
#  figure out why you selected that specific data structure.
# 'diverged': 2,
 #'in': 3,
# 'I': 8

import pandas as pd
import string
from collections import defaultdict

class hashtable:
    def __init__(self) -> None:
        self.my_dict=defaultdict(list)

    def GetData(self,datafile):
        data=pd.read_fwf(datafile)
        data.loc[-1] = data.columns.values
        data.sort_index(inplace=True)
        data.reset_index(drop=True, inplace=True)
        data=data.rename(columns={'Two roads diverged in a yellow wood,':'dta'})
       #the above have processed our data to have a new column name and set our first line free
        count=''
        for row in data.iterrows():
            my_list=data['dta'].to_list()
        new_arr=[]  
        for sentence in my_list:
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            sentence = sentence.translate(str.maketrans("—", " "))
            count=count+ ' '+ sentence 
        count=count.split()
        
        
        for word in count:
            sorted_string=tuple(sorted(word))
            self.my_dict[sorted_string].append(word)
        
               
        for value in  self.my_dict.values():
            new_arr.append(value)  
        for arr in new_arr:
            print(str(arr[0])+' : '+str(len(arr)))      
        
        
if __name__=='__main__':
    item=hashtable()
    datafile="poem.txt"
    item.GetData(datafile)