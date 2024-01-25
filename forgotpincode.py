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
            count+=1
            i1+=1

        
            
        
        print('next')
        print(self.possiblearr1)


if __name__=='__main__':
    item=passcode()
    item.possible()
