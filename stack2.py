#Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
#is_balanced("({a+b})")     --> True
#is_balanced("))((a+b}{")   --> False
#is_balanced("((a+b))")     --> True
#is_balanced("))")          --> False
#is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

from collections import deque

class stack:
    def __init__(self):
        self.container=deque()
    
    def push(self, data):
        self.container.append(data)
        return list(self.container)

    def pop(self):
        return self.container.pop()

item=stack()
def parenthesis_checker(string):
    lstr=''
    for str in string:
        item.push(str)

    while len(item.container)!=0:
        val=item.pop()
        if val== '{' or val== '}' or val== '['or val== ']' or val== '(' or  val== ')':
            lstr+=val
    
    if lstr[0]=='{' or lstr[0]=='['  or lstr[0]=='(':
        return('unbalanced')
        
    #print(lstr[0])

#string ="({a+b})"
string ="))((a+b}{"
#string ="))"
#string ="((a+b))"
#string ="[a+b]*(x+2y)*{gg+kk}"
parenthesis_checker(string)