#2. Write a Python program to find the size of a singly linked list.

class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None   # initialise  an empty head
    
    
    def add_at_beginning(self,data):
        node=Node(data,self.head) # the node class above takes 2 args, data and what comes next, since we are placing 
                                  #in the beginning, then the head becomes the next
        self.head=node
    
    
    def add_at_the_end(self,data):
        if self.head is None:
            node=Node(data,None) #if the ll is empty then the next is none and dat ais added
            self.head=node
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        #the above while iterates until there's no itr.next no more. after which we now add the next
        node = Node(data,None) # since its at the end, next is none
        itr.next=node  #synonymous to self.head.next, takes care for when the head is empty...

    

    def insert_a_list(self, data_list):
        self.head = None
        for data in data_list:
            self.add_at_the_end(data)

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

    def get_size(self):
        count =0
        itr=self.head
        while itr:
            
            count+=1
            itr=itr.next
        print(count) 

if __name__=='__main__':
    ll=LinkedList()
    
    ll.add_at_the_end(90)
    ll.printing()
    ll.insert_a_list([3,6,8,10])
    ll.printing()
    ll.get_size()
    