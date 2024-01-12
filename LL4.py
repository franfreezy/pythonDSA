#4. Write a Python program to access a specific item in a singly linked list using index value.
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        
        itr=self.head
        llstr='' # initialise an empty string
        while itr:
            llstr += str(itr.data)+ '---'
            itr=itr.next
        print(llstr) #this string prints our llinked list sperated by the lines for delimination

    def addTobeginning(self,data):
        node = Node(data,self.head)
        self.head=node

    

if __name__=='__main__':
    ll=LinkedList()
    ll.addTobeginning(1)
    ll.print()
        