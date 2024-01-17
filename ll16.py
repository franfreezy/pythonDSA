#2. Implement doubly linked list. The only difference with regular linked list
#  is that double linked has prev node reference as well. 
# That way you can iterate in forward and backward direction.
#Your node class will look this this,

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Add following new methods,
class linkedlist(self):

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        pass

    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        pass
#Implement all other methods in [regular linked list class]