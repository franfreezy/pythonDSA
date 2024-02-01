#2. Write a py program to reverse the elements of a queue.

from collections import deque
class queue:
    def __init__(self):
        self.container=deque()

    def enqueue(self,value):
        self.container.appendleft(value)
        return list(self.container)
    
    def dequeue(self):
        if self.size()==0:
            return 'queue is empty'

        self.value=self.container.pop()
        return list(self.container)

    def size(self):
        return len(self.container)

    def reverse(self):
        self.container_copy=list(self.container)
        while self.size()!=0:
            self.dequeue()
            
            
        
        for value in self.container_copy:
            self.enqueue(value)
            
        return list(self.container)
       

item=queue()


if __name__=='__main__':
    print(item.dequeue())
    item.enqueue(23)
    item.enqueue(5)
    item.enqueue(2)
   
    item.enqueue(23)
    item.enqueue(23)
    item.enqueue(9)
    print(item.enqueue(20))
    
    print(item.reverse())
    