#5. Write a py program to find the average of all elements of a queue.
# let's just extend the class from previous py file

from queue7 import queue

class queue2(queue):
    def average(self):
        average=self.summation()/(len(self.container))
        return average

item=queue2()
if __name__=='__main__':
    item.enqueue(23)
    item.enqueue(4)
    item.enqueue(5)
    item.enqueue(7)
    item.enqueue(8)
    print(item.enqueue(7))
    print(item.summation())
    print(item.average())


