#9. Write a Python program to create a doubly linked list and print nodes from current position to first node.
class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 #initialises to 0
    
    def append(self,data):
        pass
    def prepend(self,data):
        pass
    def print(self):
        pass