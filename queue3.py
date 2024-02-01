#PROBLEM STATEMENT
#Given a stack of boxes in different colors. 
# Write a python function that accepts the stack of boxes and 
# removes those boxes having color other than the primary 
# colors (Red, Green and Blue) from the stack. 
# The removed boxes should be en-queued into a new queue and returned. 
# The original stack should have only the boxes having primary 
# colors and the order must be maintained.
#Perform case sensitive string comparison wherever necessary.
#Note: Consider the queue to be of the same size as that of the original stack.**
########################################################################################
from collections import deque


class queue:
    def __init__(self):
        self.container=deque()

    def enqueue(self,value):
        
        return self.container.appendleft(value)
    
    def dequeue(self):
        if len(self.container)==0:
            print('Empty and empty and empty')
            return
        
        return self.container.pop()
    
item=queue()

def sorting_add(colorArray):
    for color in colorArray:
        item.enqueue(color)
    return list(item.container)

def sorting_remove(primaryColours):
    for color in item.container:
        print(color)

if __name__=='__main__':
    colorArray = [
  'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet',
  'White', 'Black', 'Gray', 'Brown', 'Pink', 'Purple', 'Turquoise',
  'Lavender', 'Cyan', 'Magenta', 'Maroon', 'Navy', 'Olive', 'Teal',
  'Peach', 'Beige', 'Gold', 'Silver', 'Bronze', 'Turquoise', 'Rose',
  'Ruby', 'Emerald', 'Sapphire', 'Amethyst', 'Topaz', 'Pearl', 'Opal',
  'Coral', 'Aqua', 'Lime', 'Lemon', 'Tangerine', 'Plum', 'Cherry',
  'Chocolate', 'Mint', 'Slate', 'Charcoal', 'Ivory', 'Periwinkle',
  'Azure', 'Cerulean', 'Mustard', 'Burgundy', 'Salmon', 'Sienna',
  'Steel', 'Tan', 'Crimson', 'Mauve', 'Sunset', 'Sky', 'Forest',
  'Ocean', 'Fire', 'Earth', 'Sand', 'Clay', 'Snow', 'Smoke', 'Coal'
]
primaryColours=['Red', 'Green' , 'Blue']
print(sorting_add(colorArray))
sorting_remove(primaryColours)