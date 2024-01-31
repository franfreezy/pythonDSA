#Design a food ordering system where your python program will run two threads,

#Place Order: This thread will be placing an order and inserting that into a queue.
# This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#$Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it.
#This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
#Use this video to get yourself familiar with multithreading in python

#Pass following list as an argument to place order thread,

#orders = ['pizza','samosa','pasta','biryani','burger']
#This problem is a producer,consumer problem where place_order thread is producing orders 
# whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
from collections import deque

# queue works on the FIFO basis

class queue:
    def __init__(self):
        self.container=deque()

    def AddQueue(self,data):
        self.container.appendleft(data)
        return self.container

if __name__=='__main__':
    item=queue()
    item.AddQueue('jane')
    print(item.AddQueue('frandel'))