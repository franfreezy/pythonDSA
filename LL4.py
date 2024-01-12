#4. Write a Python program to access a specific item in a singly linked list using index value.
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        
        itr=self.head
        llstr='' # initialise an empty string
        while itr:
            llstr += str(itr.data)+ '---'
            itr=itr.next
        print(llstr) #this string prints our llinked list sperated by the lines for delimination

    def addTobeginning(self,data):
        node = Node(data,self.head)
        self.head=node

    def addAtTheEnd(self,data):

        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def addAList(self,dataList):  #this actually makes our list empty first before adding our list
        self.head=None 
        for data in dataList:
            self.addAtTheEnd(data)

    #lemme try adding to a list with values
    def addToList(self,dataList):  #this actually makes our list empty first before adding our list
        #removing the initialisation of self.head to none solves it.
        for data in dataList:
            self.addAtTheEnd(data) 
    ## now lets solve our problem
    def getSize(self):
        count=0
        itr=self.head

        while itr:  #with itr we have the correct length unlike missing one with itr.next
            count+=1
            itr=itr.next
        return (count)  #this return must be here so as not to affect calling of this funtion to another method

    def AccessingBasedOnIndex(self,index):
        if index==0:
            print(self.head.data) #without the data it prints the location
                                  #to print in othe location we need a function to get the length
            return
        if index < 0 or index >self.getSize():
            print('invalid index')
            return
        
        count=0
        itr=self.head
        while count!=index-1: #must be one less so that we do not get a null as the result
            count+=1
            itr=itr.next
        print(itr.data)
        

   

            
            
            

if __name__=='__main__':
    ll=LinkedList()
    
    ll.addTobeginning(1)
    
    ll.addAtTheEnd(7)
    ll.addToList([2,3])
    
    ll.print()

    print(ll.getSize())
    ll.AccessingBasedOnIndex(3)
    
        