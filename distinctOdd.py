#Write a short Python function that takes a sequence of integer values and
#determines if there is a distinct pair of numbers in the sequence whose
#product is odd
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
            pair = myArray[i] *  myArray[k]
            
            if pair%2 == 1:
                print(str(myArray[i]) + ' * '+str(myArray[k])+ ' results to '+ str(pair) )
                    
            k=k+1
        i=i+1

    
Distinct(n)
