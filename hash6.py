#Insertion of keys into hash table using linear probing as collision resolution technique –
#Que – 2. The keys 12, 18, 13, 2, 3, 23, 5 and 15 are inserted into an initially 
# empty hash table of length 10 using open addressing with hash function h(k) = k mod 10 
# and linear probing. What is the resultant hash table? 
class hashtable:
    def __init__(self):
        self.max_value=10
        self.keysArr=[[] is None for i in range(self.max_value)]
    
    def getHash(self,keysArr):
        for key in keysArr:
            #hash(key)- the notion that we have an inbuilt hash function falls flat
            print()

if __name__=='__main__':
    item=hashtable()
    keysArr=[12, 18, 13, 2, 3, 23, 5 , 15]
    item.getHash(keysArr)