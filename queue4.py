#1. Write a py program to implement a queue using an array with enqueue and dequeue operations. 
# Find the top element of the stack and check if the stack is empty, full or not.


class queue:
    def __init__(self):
        self.myarray=[]

    def addtoQueue(self,value):
        self.myarray.insert(0,value)
        return self.myarray


item=queue()

if __name__== "__main__":
    print(item.addtoQueue(2))