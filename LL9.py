#9. Write a Python program to create a doubly linked list and print nodes from current position to first node.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 #initialises to 0
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            
            self.head=new_node
            self.tail=new_node
            return
        else:
            current=self.tail
            current.next=new_node #next value after the tail is our data
            new_node.prev=current #doubly links our list, the prev value to our data is self.tail
            self.tail=new_node # our data becomes self.tail
        
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            
            self.head=new_node
            self.tail=new_node
            return
        else:

            current=self.head
            current.prev=new_node #prev value after the head is our data
            new_node.next=current #doubly links our list, the prev value to our data is self.tail
            self.head=new_node # our data becomes self.tail

    def printf(self):
        current=self.head
        dllstr=''
        self.size=0
        while current:
            dllstr+=str(current.data)+'---'
            current=current.next
            self.size+=1
        print(dllstr)
        print('size:'+ str(self.size))


    def Testpoint(self,index):
        current=self.head
        count=0
        if index<0 or index>self.size:
            raise Exception('invalid index')
            return

        while index!=count:
            count+=1
            current=current.next
          
        self.tail=current #make sure the assignment logically is sensible
       


            

        

    
    def printb(self):
        current=self.tail
        dllstr=''
        self.size=0
        while current:
            dllstr+=str(current.data)+'---'
            current=current.prev
            self.size+=1
        print(dllstr)
        print('size:'+ str(self.size))
        

dll=dLinkedList()
dll.append(4)
dll.append(41)
dll.append(14)
dll.prepend(10)
dll.prepend(100)
dll.printf()
print('testing our method out')
dll.Testpoint(2)
dll.printb()