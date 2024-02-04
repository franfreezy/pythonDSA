'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self,head,tail):
        self.head=None
        self.tail=None