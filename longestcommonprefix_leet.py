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
        
        while len(my_dict)<=1:

            for str in strs:
                if str[i]==key:
                    
                    my_dict[key].append(str)

            i+=1    
                
                
                
            
            print (my_dict)
            break
        
            
        
        
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
item=Solution()
item.longestCommonPrefix(strs)