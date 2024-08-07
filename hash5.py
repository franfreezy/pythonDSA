#Que – 1. Given the following input (4322, 1334, 1471, 9679, 1989, 6171, 6173, 4199) 
# and the hash function x mod 10, which of the following statements are true? (GATE CS 2004) 
#i. 9679, 1989, 4199 hash to the same value -true 9
#ii. 1471, 6171 hash to the same value -true 1
#iii. All elements hash to the same value -false
#iv. Each element hashes to a different value -false
#(A) i only 
#(B) ii only 
#(C) i and ii only -correct answer
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

##to answer this question then we have to come up with the hash function
#

class hashtable:
    def __init__(self,valArr):
        self.max_value=10 
        self.myArray=[[] for i in range(self.max_value)] #this helps solve collisions alongside append()
        #without this then we will not be 
        #alllowed to append any values
        #we will get either of the 2 errors
        #none type or index error
        

    def gethash(self,value):
        h=0
        for value in valArr:
            #to hash an integer, we take the integer and get the modulus of the entire int
            #this is so because we cannot iterate over an integer but we can with strings
            h=value%self.max_value
            print(h)
            print(value)
            self.myArray[h].append(value)#solves collisions alongside []
        print(self.myArray)

if __name__=='__main__':
    valArr=[4322, 1334, 1471, 9679, 1989, 6171, 6173, 4199]
    item=hashtable(valArr)
    item.gethash(valArr)