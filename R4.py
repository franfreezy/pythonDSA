#function that takes a positive integer an d outputs all squares of all integers less than n

print(' a program that prints squares of numbers less than n ')

n=int(input('Enter the upper boundary: '))
k=n-1
square=0
sum=0
def squares(n):
    global k,square,sum
    
    while n>0:
        square=k*k
        n=n-1
        k=k-1
        sum=sum+square
        
    
    print('the summationof squares is' +str(sum))
squares(n)