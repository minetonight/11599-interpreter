#-*-coding:utf8;-*-
from os.path import join, dirname
from meaningHelper import getMeaning

class CardInterpreter:

    def __init__(self, card):
        self.card = card
    #eof def
    
    def getOneMeaning(self):
        return getMeaning(self.card, "1"+str(self.card[1]))
    
    
    def getFullInterpretation(self):
        #print(dir(self)) 
        
        #get all methods of this class
        methods = [method for method in dir(self) if callable(getattr(self, method))]
        methods.remove("__init__")
        methods.remove("getFullInterpretation") 
        
        result = '' 
        
        #call all methods
        for m in methods:
            print "calling "+m
            result += getattr(self, m)()
        
        return result
        
    #eof getFullInterpretation
    

#eof class

if __name__ == "__main__":
    cardReader = CardInterpreter( [0, 
    	2, 2, 1,
    	1, 1, 1,
    	1, 1, 2] )
    	
    print(cardReader.getFullInterpretation()) 
    #print (getMeaning(cardReader.card, "test")) 
    print ("Done") 