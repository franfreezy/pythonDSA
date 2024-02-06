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
        key=strs[0][0]
        size=len(strs)
        
        while len(my_dict)<=1 :
            
            for str in strs:
                if len(key)<=1:
                    if str[i]==key:
                    
                        my_dict[key].append(str)
                    
                    if str[i]!=key:
                        print('" "')
                        return
                
                    
                else:
                    
                    if key[:-1]==str[:i]:
                        
                        my_dict[key[:-1]].append(str)
                    else:
                        return value[0]
                


                

            i+=1  
            key+=str[i]
             
            value=(list(my_dict.keys()))
            
            my_dict=defaultdict(list)   
               
        
        
            
        
            
        
        
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
item=Solution()
print(item.longestCommonPrefix(strs))