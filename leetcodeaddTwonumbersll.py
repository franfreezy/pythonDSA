'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next

        node=Node(data,None)
        itr.next=node

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr=self.head
        linked_liststr=''
        while itr:
            linked_liststr+=str(itr.data) +'---'
            itr=itr.next
        print(linked_liststr)

item=linked_list()
 
if __name__=='__main__':
    item.append(23)
    item.append(4)
    item.append(5)
    item.append(8)
    item.print()

        
