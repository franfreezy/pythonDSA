#2. Write a py program to reverse the elements of a queue.

from collections import deque
class queue:
    def __init__(self):
        self.container=deque()

    def enqueue(self,value):
        self.container.appendleft(value)
        return list(self.container)

    def dequeue(self):
        if self.size==0:
            return 'queue is empty'

        self.value=self.container.pop()
        return self.value
    def size(self):
        return len(self.container)

    def reverse(self):
        pass
item=queue()


if __name__=='__main__':
    pass