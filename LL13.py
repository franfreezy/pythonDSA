#13. Write a Python program to search a specific item in a given doubly linked list 
# and return true if the item is found otherwise return false.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self, data):
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
    def search(self,data):
        current=self.head
        node=Node(data)
        while current:
            if current.data==node.data:
                print(True) 
                break
            
            current=current.next
        
       



if __name__=='__main__':
    dll=dLinkedList()
    dll.append(6)
    dll.append(23)
    dll.append(61)
    dll.append(67)
    dll.print()
    dll.search(23)