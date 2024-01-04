print ('a program that outputs the boolean state of whether two numbers are multiples')

n = int(input('enter a number n:'))
m = int( input('enter second number to check if it is multiple of n: '))

def is_multiple(n,m):
    if (n%m ==0):
        return True
    
    else:
        return False 

print(is_multiple(n,m))
