class CardInterpreter:

    def __init__(self, card):
        self.card = card
    #eof def
    
    
    def getFullInterpretation(self):
        pass
    
    #eof def getFullInterpretation
    
    
        
#eof class


cardReader = CardInterpreter( [0, 2, 2,1,
	1, 1, 1,
	1, 1, 2] )
cardReader.getFullInterpretation()