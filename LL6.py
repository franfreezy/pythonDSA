
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
        while itr.next:
            llstr += str(itr.data)
            itr=itr.next
        print(llstr)


    def addAtTheEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    def addAList(self,dataList):
        self.head=None
        for data in dataList:
        
    def removeFirst(self, index,data)