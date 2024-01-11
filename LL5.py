#5. Write a Python program to set a new value of an item in a singly linked list using index value.
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        