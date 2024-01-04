#function that takes a positive integer an d outputs all squares of odd integers less than n

print(' a program that prints squares of numbers less than n ')

n=int(input('Enter the upper boundary: '))
k=n-1

square=0
sum=0
def squares(n):
    global k,square,sum
    
    if(n<0):
        print('please enter a positive integer')

    if(k%2 == 1):
        while k>0:
            square=k*k
            
            k=k-2
        
            sum=sum+square
            
        print('the summation of squares is ' +str(sum))
        
    
    
squares(n)