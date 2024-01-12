#5. Write a Python program to set a new value of an item in a singly linked list using index value.
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
    
    def getSize(self):
        count=0
        itr=self.head

        while itr:  #with itr we have the correct length unlike missing one with itr.next
            count+=1
            itr=itr.next
        return (count)  #this return must be here so as not to affect calling of this funtion to another method

## now lets solve our problem
#we are deleting a current holder and assigning that place a new value
    def setANewValue(self,index,data):
        if index < 0 or index >self.getSize():
            print('invalid index')
            return

        if index==0:
            itr=self.head
            node = Node(data,self.head)
            
            
            while itr:
                itr=node

            print(itr) 
            
                
                
            
            
            
            

        



if __name__=='__main__':
    ll=LinkedList()
    
    ll.addTobeginning(1)
    
    ll.addAtTheEnd(7)
    ll.addToList([2,3])
    
    ll.print()
    ll.setANewValue(0,9)
    
    
    
    