#12. Write a Python program to insert an item in front of a given doubly linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        
        current=self.head
        current.prev=new_node
        new_node.next=current
        self.head=new_node  

    def append(self,data):#this inserts infront of a given list but we want to add somewhere in the middle
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        
        current=self.tail
        current.next=new_node
        new_node.prev=current
        self.tail=new_node

    def insert(self,index,data):
        if index==0:
            self.prepend(data)
            return

        count=0
        current=self.head
        new_node=Node(data)
        llstr=''
        while current:
            llstr+=str(current.data)+'---'
            if count==index-1:
                tmp=current.next
                current.next=new_node
                new_node.next=tmp
                new_node.prev=current
                
                
                
                break
                
        
            current=current.next
            count+=1
       
        
        
    
    def printf(self):
        current=self.head
        dllstr=''
        self.size=0
        while current:
            dllstr+=str(current.data)+'---'
            current=current.next
            self.size+=1
        print(dllstr)


if __name__=='__main__':
    dll=dLinkedList()
    dll.append(5)
    dll.append(15)
    dll.append(51)
    dll.prepend(9)
    dll.printf()
    dll.insert(3,3)
    dll.printf()