#using a fn minmax(data) check for the largest or smallest number in n numbers
#no use of inbuilt functions

print('A program that outputs largest and smallest number among n numbers')

n= int(input('How many numbers do you want to input:'))
myArray=[]
x=1
def minmax(n):
    global x
    while n>0:
        data=(int(input('enter number '+ str(x)+ ' :' )))
        myArray.append(data)
       
        n= n-1
        x=x+1
        data1=myArray[0]
        data2=myArray[0]
    for i in range(len(myArray)):
        data=myArray[i]
        if(data1 > data):
            data1 = data
        if( data > data2):
            data2 = data

    print('the smallest number is: ' + str(data1))
    print('the largest number is: '+str(data2))

minmax(n)