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
        if len(strs)==1: # takes care of one with one element
            return strs[0]
        else:
            while  i<3:
                key+=strs[0][i]
                count=0
                size=len(my_dict[key])
                print(size)
                for str in strs:
                    string=str[0:i+1]
                    
                    
                    if key==string :
                        count+=1
                        my_dict[key].append(str)
                        print(size)
                        

                
                

                i+=1
                if 
                print(my_dict)
                value=list(my_dict.keys())
                
                print(value)
                

        
        
            
        
            
        
        
#strs = ["car","cir"]
strs =["flower","flow","flight"]
#strs =["a", "a"]
#strs =[ "a"]
#strs = ["dog","racecar","car"]
#strs =["flower","flower","flower","flower"]
item=Solution()
print(item.longestCommonPrefix(strs))