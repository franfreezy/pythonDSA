#Write a function in python that can reverse a string using stack data structure. 
# Use Stack class from the tutorial.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collectons import deque

class stack:
    def __init__(self):
        self.container=deque()

    def enqueue(self,data):
        self.container.append(data)

        return list(self.container)