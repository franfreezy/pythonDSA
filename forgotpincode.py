class passcode:
    def __init__(self):
        self.max_value=10000
        self.possiblearr1=[None for i in range(int(self.max_value/10))]
        self.possiblearr2=[None for i in range(int((2*self.max_value)/10))]
        self.possiblearr3=[None for i in range(int((3*self.max_value)/10))]
        self.possiblearr4=[None for i in range(int((4*self.max_value)/10))]
        self.possiblearr5=[None for i in range(int((5*self.max_value)/10))]
        self.possiblearr6=[None for i in range(int((6*self.max_value)/10))]
        self.possiblearr7=[None for i in range(int((7*self.max_value)/10))]
        self.possiblearr8=[None for i in range(int((8*self.max_value)/10))]
        self.possiblearr9=[None for i in range(int((9*self.max_value)/10))]
        self.possiblearr10=[None for i in range(int((10*self.max_value)/10))]
    def possible(self):
        for i in range(int(self.max_value/10)):
            self.possiblearr1[i]=i
        for i in range(int(self.max_value/10),int((2*self.max_value)/10)):
            self.possiblearr2[i]=i
        for i in range(int(self.max_value/10)):
            self.possiblearr1[i]=i
        for i in range(int(self.max_value/10)):
            self.possiblearr1[i]=i
        for i in range(int(self.max_value/10)):
            self.possiblearr1[i]=i
        print('next')
        print(self.possiblearr2)


if __name__=='__main__':
    item=passcode()
    item.possible()
