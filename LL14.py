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
        current=self.head
        node=Node(data)
        count=0
        llstr=''
        while current:
            
            if current.data==node.data:
                
                if count==0:
                    
                    current=current.next
                    self.head=current
                    
                    return
                else:
                    current=current.next
                    
                    current.prev=current.prev.prev
                    
                    
            llstr+=str(current.data)+'--'
            count+=1
                    
            current=current.next
        print(llstr)    
                    
            
          
                
            
        
            
            
        

if __name__=='__main__':
    dll=dLinkedList()
    dll.append(6)
    dll.append(23)
    dll.append(61)
    dll.append(67)
    dll.print()
    dll.Remove(23)
    
    
