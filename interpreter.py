#-*-coding:utf8;-*-
from os.path import join, dirname
from meaningHelper import getMeaning

class CardInterpreter:

    def __init__(self, card):
        self.card = card
    #eof def
    
    
    def getFullInterpretation(self):
        pass
    
    #eof def getFullInterpretation
    

#eof class

if __name__ == "__main__":
    cardReader = CardInterpreter( [0, 
    	2, 2, 1,
    	1, 1, 1,
    	1, 1, 2] )
    	
    cardReader.getFullInterpretation()
    print (getMeaning(cardReader.card, "test")) 
    print ("Done") 