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
        dllstr=''
        while current:
            dllstr+=str(current.data)+'--'
            print('here')
            if count==0:
                current=current.next
                self.head=current

                return
                

            if current.data==node.data:
                new=current.next
                current=current.prev
                current.next=new
                print(new.data)
                ##print(current.prev.data)
                print(current.next.next.data)
                break
            
        
            current=current.next
            count+=1
        print(dllstr)

if __name__=='__main__':
    dll=dLinkedList()
    dll.append(6)
    dll.append(23)
    dll.append(61)
    dll.append(67)
    dll.print()
    dll.Remove(6)
    dll.print()
    
