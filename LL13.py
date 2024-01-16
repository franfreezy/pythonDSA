#13. Write a Python program to search a specific item in a given doubly linked list 
# and return true if the item is found otherwise return false.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None