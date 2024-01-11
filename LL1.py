#. Write a Python program to create a singly linked list, append some items and iterate through the list.
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
# we create an empty list to begin with

class LinkedList:
    def __init__(self):
        self.head=None   #our linked list will be set to empty


    def add_at_beginning(self,data):
        node=Node(data,self.head) # the node class above takes 2 args, data and what comes next, since we are placing 
                                  #in the beginning, then the head becomes the next
        self.head=node


    def printing(self):   # we create this method for printing purposes only....
        if (self.head==None):
            print('linked list is empty')
            return
        # we can now iterate through the list as follows
        itr=self.head  #an iterator
        llstr = ''     #an empty linked list string
        while itr:     #while we have a head we iterate thru
            llstr += str(itr.data) + '----'  # we add the data to the linked list string
            itr=itr.next
        print(llstr) # we now print when there's no more data

if __name__ =='__main__':
    ll=LinkedList()
    ll.add_at_beginning(5)
    ll.add_at_beginning(15)
    ll.add_at_beginning(54)
    ll.printing()








