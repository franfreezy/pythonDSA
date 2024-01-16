
#8. Write a Python program to create a doubly linked list, 
# append some items and iterate through the list (print forward).
class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None