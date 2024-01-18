#Que – 1. Given the following input (4322, 1334, 1471, 9679, 1989, 6171, 6173, 4199) 
# and the hash function x mod 10, which of the following statements are true? (GATE CS 2004) 
#i. 9679, 1989, 4199 hash to the same value 
#ii. 1471, 6171 hash to the same value 
#iii. All elements hash to the same value 
#iv. Each element hashes to a different value 
#(A) i only 
#(B) ii only 
#(C) i and ii only 
#(D) iii or iv 

#Solutions: Using given hash function h(x) = x mod 10 
#solution h(9679) = 9679%10 = 9 
#h(1989) = 1989%10 = 9 
#h(4199) = 4199%10 = 9 
#h(1471) = 1471%10 = 1 
#h(6171) = 6171%10 = 1 
#As we can see, 9679, 1989 and 4199 hash to same value 9. 
# Also, 1471 and 6171 hash to same value 1. Therefore,
#  statement (i) and (ii) are correct which match with option (C). 