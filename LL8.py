
#8. Write a Python program to create a doubly linked list, 
# append some items and iterate through the list (print forward).
class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev