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
            llstr += str(itr.data)+' --> '
            itr = itr.next
        print(llstr)
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        #implementation
        itr=self.head
        node=Node(data_to_insert,itr.next.next)
        
        
        while itr:
            if itr.data==data_after:
                
                itr.next=node
                break
            
            itr=itr.next

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        


    def remove_by_value(self, data):
        # Remove first node that contains data
        pass

#Now make following calls,
if __name__=='__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
   # #ll.remove_by_value("orange") # remove orange from linked list
    #ll.print()
    
    #ll.remove_by_value("figs")
    #ll.print()
    #ll.remove_by_value("banana")
    #ll.remove_by_value("mango")
    #ll.remove_by_value("apple")
    #ll.remove_by_value("grapes")
    #ll.print()