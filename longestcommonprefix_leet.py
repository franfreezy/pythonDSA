'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        my_dict=defaultdict(list)
        i=0
        key=''
        if len(strs)<1: #takes care of empty arrays
            return ''
        if len(strs[0])<1: #takes care of empty strings
            return ''
        if len(strs)==1: # takes care of one with one element
            return strs[0]
           
        
        else:
            
            while  i<len(strs[0]):
                key+=strs[0][i]
                
                
                for str in strs:
                    string=str[0:i+1]
                    print('here')
                    print(str)
                    if str=="":
                        return ""

                    if key==string:
                        
                        my_dict[key].append(str)
                        print(my_dict)
                   
                        
                        
                        
                size=len(my_dict[key])
                if size==len(strs):
                    i+=1
                else:
                    if i==0:
                        return ""
                    
                    value=list(my_dict.keys())
                    return value[-2]
                
            #value=list(my_dict.keys())
            #return value[-1]
                
                
                
                
                
                

        
        
            
        
            
        
        
#strs = ["car","cir"]
#strs =["flower","flow","flight"]
#strs =["a", "a"]
#strs =[ "a"]
strs = ["dog","racecar","car"]
strs =["",""]
#strs =["flower","flower","flower","flower"]
item=Solution()
print(item.longestCommonPrefix(strs))