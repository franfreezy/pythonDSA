
#8. Write a Python program to create a doubly linked list, 
# append some items and iterate through the list (print forward).
class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
        self.prev=prev

class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail= None

    #lets write a method for displaying
    
        #working on our challenge
    def append(self, data):
        new_node=Node(data)
        itr=self.head
            # we have two scenarios, an empty dll or non-null dll, we have to work out both
        if itr is None:
            self.head=new_node
            self.tail=new_node #this makes our list doubly.
            return



if __name__=='__main__':
    item=DLinkedList()
    item.append(5)
    print()