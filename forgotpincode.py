class passcode:
    def __init__(self):
        self.max_value=10000
        self.maxIndex=1000
        self.possiblearr1=[None for i in range(self.maxIndex)]
        self.possiblearr2=[None for i in range(self.maxIndex)]
        self.possiblearr3=[None for i in range(self.maxIndex)]
        self.possiblearr4=[None for i in range(self.maxIndex)]
        self.possiblearr5=[None for i in range(self.maxIndex)]
        self.possiblearr6=[None for i in range(self.maxIndex)]
        self.possiblearr7=[None for i in range(self.maxIndex)]
        self.possiblearr8=[None for i in range(self.maxIndex)]
        self.possiblearr9=[None for i in range(self.maxIndex)]
        self.possiblearr10=[None for i in range(self.maxIndex)]
        self.myArr=[None for i in range(self.max_value)]
    def possible(self):
        count=0
        i1=0
        i2=1000
        i3=2000
        i4=3000
        i5=4000
        i6=5000
        i7=6000
        i8=7000
        i9=8000
        i10=9000
        while count!=1000:
            self.possiblearr1[count]=f'{i1:04}'
            self.possiblearr2[count]=str(i2)
            self.possiblearr3[count]=str(i3)
            self.possiblearr4[count]=str(i4)
            self.possiblearr5[count]=str(i5)
            self.possiblearr6[count]=str(i6)
            self.possiblearr7[count]=str(i7)
            self.possiblearr8[count]=str(i8)
            self.possiblearr9[count]=str(i9)
            self.possiblearr10[count]=str(i10)
            count+=1
            i1+=1
            i2+=1
            i3+=1
            i4+=1
            i5+=1
            i6+=1
            i7+=1
            i8+=1
            i9+=1
            i10+=1

        
        self.myArr=  (self.possiblearr1  + self.possiblearr2 + self.possiblearr3 + self.possiblearr4 + self.possiblearr5 +self.possiblearr6 + self.possiblearr7+self.possiblearr8 +self.possiblearr9 +self.possiblearr10)
        for value in self.myArr:
            if value[0] =='0':
            print(value)

       


if __name__=='__main__':
    item=passcode()
    item.possible()
