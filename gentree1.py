class GeneralTree:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)
        

    def Print(self):
        distinguisher=" "*self.level_finder()
        print(distinguisher+self.data)
        if self.children:
            for child  in self.children:
                child.Print()
    
    def level_finder(self):
        count=0
        p=self.parent
        
        while p:
            count+=1
            p=p.parent
        return count #this indentation returns zero, in the while returns none

if __name__=='__main__':
    school=GeneralTree("COETEC")
    
    EEE=GeneralTree("EEE")
    EEE.addChild(GeneralTree("EEE"))
    EEE.addChild(GeneralTree("ECE"))
    TIE=GeneralTree("TIE")
    TIE.addChild(GeneralTree("TIE"))
    school.addChild(EEE)
    school.addChild(TIE)
    #print(school.level_finder())
    school.Print()

