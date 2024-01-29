#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or 
# phrase, typically using all the original letters exactly once.

 

#Example 1:

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

##implementation
from collections import defaultdict
class anagram():
    def __init__(self,strs):
        self.strs=strs

    
    def sorter(self):
        my_dict=defaultdict(list) #this ensures that the sorted string is made key
        
        for str in self.strs:
            sort=tuple(sorted(str))
            
            my_dict[sort].append(str)
            print(my_dict)

if __name__=='__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    item=anagram(strs)
    item.sorter()