#11. Write a Python program to print a given doubly linked list in reverse order.
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
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        
        current=self.tail
        current.next=new_node
        new_node.prev=current
        self.tail=new_node


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
    
    def normalOrder(self):
        current=self.head
        dllstr=''

        while current:
            dllstr+=str(current.data)+ '----'
            current=current.next

        print (dllstr)

    def reverseOrder(self):
        current=self.tail
        dllstr=''

        while current:
            dllstr+=str(current.data)+ '----'
            current=current.prev

        print (dllstr)

dll=dLinkedList()
dll.append(3)
dll.append(23)
dll.append(31)
dll.prepend(4)
dll.prepend(2)
dll.normalOrder()
print('now reversed')
dll.reverseOrder()