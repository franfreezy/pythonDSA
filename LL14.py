#14. Write a Python program to delete a specific item from a given doubly linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
            return
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node

    def print(self):
        current=self.head
        dllstr=''
        while current:
            dllstr+=str(current.data)+'----'
            current=current.next
        print (dllstr)
  ##implementation      
    def Remove(self, data):
        new=self.head
        node=Node(data)
        count=0
        
        while new:
            if new.data==node.data:
                if count==0:
                    new=new.next
                    self.head=new
                    return
                else:
                    tmp=current.prev
                    print('here')
                    current.prev=tmp
                    current=current.next
                    count+=1
                    return
                    
                 
                    
            
          
                
            
        
            
            
        

if __name__=='__main__':
    dll=dLinkedList()
    dll.append(6)
    dll.append(23)
    dll.append(61)
    dll.append(67)
    dll.print()
    dll.Remove(6)
    dll.print()
    
