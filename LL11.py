#11. Write a Python program to print a given doubly linked list in reverse order.
class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev