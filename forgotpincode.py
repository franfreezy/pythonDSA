class passcode:
    def __init__(self):
        self.max_value=10000
        self.possiblearr1=[None for i in range(int(self.max_value/10))]
        self.possiblearr2=[None for i in range(int((2*self.max_value)/10))]
        self.possiblearr3=[None for i in range(int(self.max_value/10))]
        self.possiblearr4=[None for i in range(int(self.max_value/10))]
        self.possiblearr5=[None for i in range(int(self.max_value/10))]
        self.possiblearr6=[None for i in range(int(self.max_value/10))]
        self.possiblearr7=[None for i in range(int(self.max_value/10))]
        self.possiblearr8=[None for i in range(int(self.max_value/10))]
        self.possiblearr9=[None for i in range(int(self.max_value/10))]
        self.possiblearr10=[None for i in range(int(self.max_value/10))]
    def possible(self):
        for i in range(int(self.max_value/10)):
            self.possiblearr1[i]=i
        print(str(self.max_value)+ ' trials ')
        print(self.possiblearr1)


if __name__=='__main__':
    item=passcode()
    item.possible()
