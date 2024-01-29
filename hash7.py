#Given a hash table with keys, verify/find possible sequence of keys leading to hash table
#Que – 3. A hash table of length 10 uses open addressing with hash function h(k)=k mod 10, and linear probing.
#  After inserting 6 values into an empty hash table, the table is as shown below. 
#Which one of the following choices gives a possible order in which the key values could have been inserted in the table? 
#(A) 46, 42, 34, 52, 23, 33 
#(B) 34, 42, 23, 52, 33, 46 
#(C) 46, 34, 42, 23, 52, 33 
#(D) 42, 46, 33, 23, 34, 52 

#Solution: We will check whether sequence given in option A can lead to hash table given in question. 
# Option A inserts 46, 42, 34, 52, 23, 33 as: 

#For key 46, h(46) is 46%10 = 6. Therefore, 46 is placed at 6th index in the hash table. 
#For key 42, h(42) is 42%10 = 2. Therefore, 42 is placed at 2nd index in the hash table. 
#For key 34, h(34) is 34%10 = 4. Therefore, 34 is placed at 4th index in the hash table. 
#For key 52, h(52) is 52%10 = 2. However, index 2 is occupied with 42. Therefore, 52 is placed at 3rd index in the hash table. But in given hash table, 52 is placed at 5th index. Therefore, sequence in option A can’t generate hash table given in question. 

#In the similar way, we can check for other options as well which leads to answer as (C). 

## the implementation
class hashtable:
    def __init__(self):
        self.max_value=10
        self.myArr=[None for i in range(self.max_value)]