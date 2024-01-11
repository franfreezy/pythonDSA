#Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

#THE IMPLEMENTATION

print('a program that prints odd numbers ')

num=int(input('Enter the max number you are interested with:'))
mylist=[]
def OddFinder(num,mylist):
    for i in range (num):
        if (i %2) != 0:
            mylist.append(i)
        
    return mylist

print(OddFinder(num,mylist))

