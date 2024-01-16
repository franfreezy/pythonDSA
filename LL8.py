
#8. Write a Python program to create a doubly linked list, 
# append some items and iterate through the list (print forward).
class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
        self.prev=prev

class DLinkedList:
    def __init__(self):
        self.head=None

    #lets write a method for displaying
    def print(self):
        if self.head is None:
            print('doubly linked list empty')
            return

        itr=self.head
        dllstr=''
        while itr:
            dllstr+= str(itr)+ '----'
            itr=itr.next
            return
            