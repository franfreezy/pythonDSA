### ex
    # Exercise: Linked List

#1. In [LinkedList class]
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        #implementation
        itr=self.head
        node=Node(data_after)
        count=0
        while itr:
            if current.data==node.data:
                tmp=current.next
                current.next=node.data
                current.next.next=tmp


        


    def remove_by_value(self, data):
        # Remove first node that contains data
        pass

#Now make following calls,
if __name__=='__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
   # ll.print()
   # #ll.remove_by_value("orange") # remove orange from linked list
    #ll.print()
    
    #ll.remove_by_value("figs")
    #ll.print()
    #ll.remove_by_value("banana")
    #ll.remove_by_value("mango")
    #ll.remove_by_value("apple")
    #ll.remove_by_value("grapes")
    #ll.print()