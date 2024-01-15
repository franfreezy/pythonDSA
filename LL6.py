
#6. Write a Python program to delete the first item from a singly linked list.
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    #a method to print
    def print(self):
        if self.head is None:
            print('linked list is empty')
            return

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data)+ '----'
            itr=itr.next
        print(llstr)
    

    def addAtTheEnd(self,data):
        if self.head is None:
            node=Node(data,None) #if the ll is empty then the next is none and dat ais added
            self.head=node
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        #the above while iterates until there's no itr.next no more. after which we now add the next
        node = Node(data,None) # since its at the end, next is none
        itr.next=node  #synonymous to self.head.next, takes care for when the head is empty...

        
    def addAList(self,dataList):
        self.head=None
        for data in dataList:
            self.addAtTheEnd(data)
        
    def removeFirst(self, index):
        itr=self.head
        if index==0:
            
            self.head=itr.next

ll=LinkedList()

ll.print()
ll.addAList([1,3,5,6,7])
ll.print()
ll.addAtTheEnd(6)
ll.removeFirst(0 )
ll.print()
