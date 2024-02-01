#6. Write a py program to find the median of all elements of a queue.

from queue5 import queue

class Queue(queue):
    def medianFind(self):
        size=self.size()
        if size%2==0:
            middle=int(size/2)
            print(str(self.container[middle])+ ' and '+str(self.container[middle-1]) )


item=Queue()

if __name__=='__main__':
    item.enqueue(23)
    item.enqueue(4)
    item.enqueue(5)
    item.enqueue(7)
    item.enqueue(8)
    print(item.enqueue(7))
    item.medianFind()