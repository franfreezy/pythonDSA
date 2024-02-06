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
        if strs[0]:
            key=strs[0][0]
            if len(strs)==1:
                return strs[0]
        
        
            while len(my_dict)<=1 :

                for str in strs:
                    if len(key)<=1:
                        if str[i]==key and len(str)==1:
                        
                            return str[i]

                        if str[i]!=key:
                            empty_string = ""
                            return empty_string


                    else:
                        

                        if key[:-1]==str[:i]:

                            my_dict[key[:-1]].append(str)
                        else:
                            return value[0]





                i+=1  
                key+=str[i]

                value=(list(my_dict.keys()))

                my_dict=defaultdict(list)   

        else:
            return ""       
        
        
            
        
            
        
        
#strs = ["frlower","flow","flight"]
#strs = ["dog","racecar","car"]
strs =["ab", "a"]
item=Solution()
print(item.longestCommonPrefix(strs))