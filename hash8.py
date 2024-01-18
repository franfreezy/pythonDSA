#Que – 4. How many different insertion sequences of the key values using the same hash function
#  and linear probing will result in the hash table given in Question 3 above? 
#(A) 10 
#(B) 20 
#(C) 30 
#(D) 40 

#Solution: The first key which is not at the index computed by hash function is 52. 
# It means index 2, 3 and 4 were already occupied and therefore, key 52 is placed at index 5. 

#The keys 42, 23 and 34 are present at index 2, 3, and 4 respectively. As these keys are at their
#  correct position, their order of insertion does not matter. These 3 keys can be inserted in 3! = 6 ways. 
# Therefore, the sequence will be any order of (42, 23, 34) followed by 52. 

#The next key which is not at the index computed by hash function is 33. It means indexes 3 to 6 were already 
# occupied and key 33 is placed at index 7. Therefore, it is the last key to be inserted into hash table. 

#The key 46 is present at its correct position computed by hash function. Therefore, it can be inserted 
# at any place in the sequence before 33. The sequence excluding 33 has 4 elements 42, 23, 34, 52 which 
# create 5 positions for 46 (3 in-between and 2 corners). 
#Total number of ways is: 6*5 =30 

#Type 4: Chaining based collision resolution technique – 
#In chaining based collision resolution technique, the keys generating same hash value are placed in same 
# bucket using pointers. The different types of questions based on chaining technique are: 