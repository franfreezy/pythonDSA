#1. Write a py program to implement a queue using an array with enqueue and dequeue operations. 
# Find the top element of the stack and check if the stack is empty, full or not.

#important notes- Queue -FIFO. top element= first in

class queue:
    def __init__(self):
        self.max_size=10
        self.myarray=[ None for i in range(self.max_size)]
       

    def addtoQueue(self,value):
        if all(value is not None for value in self.myarray):
            
            return self.full(),(str(value)+' not added to queue')
        
        self.myarray.insert(0,value)
        while len(self.myarray)>self.max_size:
            self.dequeue()

        return self.myarray

    def dequeue(self):
        if all(value is None for value in self.myarray):
            return 'queue is empty' # checks for not empty.. for full we have to assign our array a size
        
        self.myarray.pop()
        return self.myarray

    def top_element(self):
        size=len(self.myarray)-1
        

        while self.myarray[size] is None:
            
            
            size=size-1
        return self.myarray[size]

        
        top_element=self.myarray[size]
        return top_element
    
    def full(self):
        
        return 'queue is full'
            


            
item=queue()

if __name__== "__main__":
    print(item.dequeue())
    item.addtoQueue(14)
    item.addtoQueue(9)
    item.addtoQueue(10)
    item.addtoQueue(23)
    item.addtoQueue(213)
    item.addtoQueue(231)
    item.addtoQueue(23)
    item.addtoQueue(3)
    
    item.addtoQueue(5)
    
    print(item.addtoQueue(2))
    print(item.addtoQueue(5))
    print(item.top_element())
    
    
    #print(item.full())