#1. Write a py program to implement a queue using an array with enqueue and dequeue operations. 
# Find the top element of the stack and check if the stack is empty, full or not.

#important notes- Queue -FIFO. top element= first in

class queue:
    def __init__(self):
        self.myarray=[]
       

    def addtoQueue(self,value):
        self.myarray.insert(0,value)
        return self.myarray

    def dequeue(self):
        if len(self.myarray)==0:
            return 'queue is empty'
        
        self.myarray.pop()
        return self.myarray
    def top_element(self):
        top_element=self.myarray[-1]
        return top_element
item=queue()

if __name__== "__main__":
    print(item.dequeue())
    item.addtoQueue(23)
    item.addtoQueue(3)
    item.addtoQueue(5)
    print(item.top_element())
    print(item.addtoQueue(2))
    print(item.top_element())
    
    print(item.dequeue())
    print(item.top_element())