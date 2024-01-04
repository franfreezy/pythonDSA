#Write a short Python program that takes two arrays a and b of length n
#storing int values, and returns the dot product of a and b. That is, it returns
#an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
print('A program that outputsan array that is a cross product of 2 arrays')
a=[]
b=[]
c=[]
n=int(input('Enter the size of your array: '))
k=0
f=1
dataA=0
dataB=0
dataC=0
def ArrayMultiplier(n):
    global a,b,c,k,f,dataA,dataB,dataC
    while k < n:
        dataA=int(input('Array1: enter number '+str(f)+' : '))
        dataB=int(input('Array2: enter number '+str(f)+' : '))
        f=f+1
        k=k+1
        a.append(dataA)
        b.append(dataB)
    
    for i in range(len(a)):
        dataC=a[i] * b[i]
        c.append(dataC)
    print(a)
    print(b)
    print(c)
ArrayMultiplier(n)