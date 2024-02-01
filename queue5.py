#2. Write a py program to reverse the elements of a queue.

from collections import deque
class queue:
    def __init__(self):
        self.container=deque()

    def enqueue(self,value):
        self.container.appendleft(value)
        return list(self.container)