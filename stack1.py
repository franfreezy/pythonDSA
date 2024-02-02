#Write a function in python that can reverse a string using stack data structure. 
# Use Stack class from the tutorial.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque

class stack:
    def __init__(self):
        self.container=deque()

    def push(self,data):
        self.container.append(data)

        return list(self.container)

    def pop(self):
        return self.container.pop()

item1=stack()


def string_reverse(string):
    
    for str in string:
        item1.push(str)
    rev_str=''    
    for value in list(item1.container):
        
        val=item1.pop()
        rev_str+=val
    print(rev_str)
        
    
string="We will conquere COVID-19"
string_reverse(string)