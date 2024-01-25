class passcode:
    def __init__(self):
        self.max_value=10000
        self.possiblearr=[None for i in range(self.max_value)]
    
    def possible(self):
        print(str(self.max_value)+ ' trials ')
        print(self.possiblearr)


if __name__=='__main__':
    item=passcode()
    item.possible()
