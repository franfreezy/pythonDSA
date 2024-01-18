#Type 4: Chaining based collision resolution technique – 
#In chaining based collision resolution technique, the keys generating same hash value are placed in same 
# bucket using pointers. The different types of questions based on chaining technique are: 

#Que – 5. Consider a hash table with 100 slots. Collisions are resolved using chaining. 
# Assuming simple uniform hashing, what is the probability that the first 3 slots are unfilled 
# after the first 3 insertions? (GATE-CS-2014) 
#(A) (97 × 97 × 97)/100^3 
#(B) (99 × 98 × 97)/100^3 
#(C) (97 × 96 × 95)/100^3 
#(D) (97 × 96 × 95)/(3! × 100^3) 

#Solution: In uniform hashing, the function evenly distributes keys into slots of hash table. 
# Also, each key has an equal probability of being placed into a slot, being independent of the other 
# elements already placed. 

#Therefore, the probability of remaining first 3 slots empty for first insertion 
# (choosing 4 to 100 slot) = 97/100. As next insertions are independent on previous insertion,
#  the probability for next insertions will also be 97/100. The required probability will be (97/100)^3. 