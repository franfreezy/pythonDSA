#4. Write a py program to find the sum of all elements of a queue.

from collections import deque
class queue:
    def __init__(self):
        self.container=deque()

    def enqueue(self,data):
        self.container.appendleft(data)
        return list(self.container)
    
    def summation(self):
        sum=0
        for value in self.container:
            sum+=value
        return sum

item =queue()

if __name__ =='__main__':
    item.enqueue(23)
    item.enqueue(4)
    item.enqueue(5)
    item.enqueue(7)
    item.enqueue(8)
    print(item.enqueue(7))
    print(item.summation())