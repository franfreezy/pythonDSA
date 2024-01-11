#3. Write a Python program to search a specific item in a singly linked list and return true if the item is
#  found otherwise return false.
class Node:
    def __init__(self, data,next):
        self.data =data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    #a method to print
    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr=self.head
        llstr=''
        while itr.next:
            llstr += str(itr.data)
            itr=itr.next
        print(llstr)

    def addInTheBeginning(self,data):
        
        node=Node(data,self.head)
        self.head=node

    def addAtTheEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    def addAList(self,dataList):
        self.head=None
        for data in dataList:
            self.addAtTheEnd(data)

    def CheckPresence(self):
        check = int(input('what are you looking for: '))
        itr=self.head
        count=0
        while itr:
            if check==itr.data:
                count+=1

            itr=itr.next
        if count==1:
            print(True) 
        else:
            print(False)   
if __name__ =='__main__':
    ll=LinkedList()
    ll.addAtTheEnd(2)
    ll.print
    ll.addAList([200,280,12,34])
    ll.print()
    ll.CheckPresence()