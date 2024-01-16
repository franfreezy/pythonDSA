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
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            self.tail=new_node
            return
        else:
            current=self.tail
            current.next=new_node #next value after the tail is our data
            new_node.prev=current #doubly links our list, the prev value to our data is self.tail
            self.tail=new_node # our data becomes self.tail
            
        
        
    def prepend(self,data):
        pass
    def print(self):
        pass