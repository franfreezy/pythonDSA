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
            self.possiblearr1[count]=i1
            self.possiblearr2[count]=i2
            self.possiblearr3[count]=i3
            self.possiblearr4[count]=i4
            self.possiblearr5[count]=i5
            self.possiblearr6[count]=i6
            self.possiblearr7[count]=i7
            self.possiblearr8[count]=i8
            self.possiblearr9[count]=i9
            self.possiblearr10[count]=i10
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

        
            
        
        print('next')
        print(self.possiblearr1)
        print('next')
        print(self.possiblearr2)
        print('next')
        print(self.possiblearr3)
        print('next')
        print(self.possiblearr4)
        print('next')
        print(self.possiblearr5)
        print('next')
        print(self.possiblearr6)
        print('next')
        print(self.possiblearr7)
        print('next')
        print(self.possiblearr8)
        print('next')
        print(self.possiblearr9)
        print('next')
        print(self.possiblearr10)


if __name__=='__main__':
    item=passcode()
    item.possible()
