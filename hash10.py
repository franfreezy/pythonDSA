#Que – 6. Which one of the following hash functions on integers will distribute keys most uniformly 
# over 10 buckets numbered 0 to 9 for i ranging from 0 to 2020? (GATE-CS-2015) 
#(A) h(i) =i^2 mod 10 
#(B) h(i) =i^3 mod 10 
#(C) h(i) = (11 ∗ i^2) mod 10 
#(D) h(i) = (12 ∗ i) mod 10 

#Solution: In uniform distribution, the function evenly distributes keys into slots of hash table. 
#For given hash functions, we have calculated hash values for keys 0 to 9 as: 
#As we can see from the table, i^3 mod10 is distributing evenly from indexes 0 to 9. 
# Other functions have not utilized all indexes. 

## the implementation
class hashtable:
    def __init__(self,multiplier):
        self.multiplier=multiplier
        self.max_value=10
        self.myArr=[[] for i in range(self.max_value)]
    
    def table(self):
        for i in self.multiplier:
            h=i%self.max_value
            self.myArr[h].append(i)
        print(self.myArr)

if __name__== '__main__':
    multiplier=range(2020)
    i=multiplier
    item=hashtable(i)
    item.table()