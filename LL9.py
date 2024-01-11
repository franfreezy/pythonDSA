#9. Write a Python program to create a doubly linked list and print nodes from current position to first node.
class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None