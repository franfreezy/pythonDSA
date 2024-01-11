#14. Write a Python program to delete a specific item from a given doubly linked list.
class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None
        
