
#8. Write a Python program to create a doubly linked list, 
# append some items and iterate through the list (print forward).
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

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
            
        else:
            
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
    
    def FWiteration(self): #prints forward
        itr=self.head
        dllstr=''
        while itr:
            dllstr += str(itr.data)+'----'
            itr=itr.next
        print (dllstr)

    def BWiteration(self): #prints backwards
        itr=self.tail
        dllstr=''
        while itr:
            dllstr += str(itr.data)+'----'
            itr=itr.prev
        print (dllstr)
           




if __name__=='__main__':
    item=DLinkedList()
    item.append(5)
    item.append(5)
    item.append(51)
    item.FWiteration()
    item.BWiteration()