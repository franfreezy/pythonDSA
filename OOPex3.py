# Write a Python program to create a calculator class. Include methods for basic arithmetic operations
print( ' a simple calculator program, basically')

operations=['1.add','2.subtract', '3.divide','4.remainder','5.multiply','6.multi-operations']
print('this calculator supports the following operations select one')
for i in range(len(operations)):
    print(operations[i])
operation=int(input('Enter selected operation: '))

num=[]
class calculator():
    
    def __init__(self,num,operation):
        self.num=num
        self.operation=operation

    def select():
        if(self.operation==1):
            ADD()
        if(self.operation==2):
            sub()
        if(self.operation==3):
            div()

        if(self.operation==4):
            rem()

        if(self.operation==5):
            mul()

        if(self.operation==6):
            multiple()

        

    def ADD(self):
        result=0
        k=1
        print('Enter the numbers you want to add then press Enter when done :')
        while True:
            num1=input()
            if num1 == '':
                break
            num2=int(num1)
            result=result+num2
            k=k+1
        return result
    def sub(self):
        result=0
        k=1
        print('Enter the numbers you want to subtract then press Enter when done :')
        while True:
            num1=input()
            if num1 == '':
                break
            num2=int(num1)
            self.num.append(num2)
            result=num[0]
            for i in range (len(num)-1):
                i=i+1
                result=result-num[i]

            
        print (result)
        



   
calc =calculator(num,operation)
sub=calc.sub()
        

