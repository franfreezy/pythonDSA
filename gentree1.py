class GeneralTree:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)
        

    def Print(self):
        print(self.data)
        if self.children:
            for child  in self.children:
                child.Print()
    
    def level_finder(self):
        

if __name__=='__main__':
    school=GeneralTree("COETEC")
    
    EEE=GeneralTree("EEE")
    EEE.addChild(GeneralTree("EEE"))
    EEE.addChild(GeneralTree("ECE"))
    TIE=GeneralTree("TIE")
    TIE.addChild(GeneralTree("TIE"))
    school.addChild(EEE)
    school.addChild(TIE)
    school.Print()

