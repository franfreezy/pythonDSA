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

    def addAtTheEnd(self,data):

        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def addAList(self,dataList):  #this actually makes our list empty first before adding our list
        self.head=None 
        for data in dataList:
            self.addAtTheEnd(data)

if __name__=='__main__':
    ll=LinkedList()
    
    ll.addTobeginning(1)
    ll.addAtTheEnd(7)
    ll.addAList([2,3])
    ll.print()
        