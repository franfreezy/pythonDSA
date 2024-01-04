#Write a Python function that takes a sequence of numbers and determines
#if all the numbers are different from each other (that is, they are distinct).
print('A program that prints if there is a distinct odd product')
n = int(input('how many numbers are in your sequence: '))
myArray=[]
f=1


def Distinct(n):
    global f
    while n>0:
        k=int(input('specify the number '+ str(f)+': '))
        myArray.append(k)
        f=f+1
        n=n-1
        
    print(myArray)
    i=0
    while i< len(myArray):
        k=i+1
        while k < len(myArray):
            
            
            if myArray[i] == myArray[k]:
                print(str(myArray[i]) + ' = '+str(myArray[k]) )
                    
            k=k+1
        i=i+1

    
Distinct(n)