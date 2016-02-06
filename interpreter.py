#-*-coding:utf8;-*-
from os.path import join, dirname
from numerology import CardCalculator 

class CardInterpreter:

    def __init__(self, cardCalculator, readingType):
        self.card = cardCalculator.card
        self.readingType = readingType
    #eof __init__
    
    
    def getMeaning(self, buttonName):
        # TODO check buttons types 
        return self._getMeaning("1"+str(self.card[1]))
    
    
    def getFullInterpretation(self):
        #print(dir(self)) 
        
        #get all methods of this class
        buttons = ["1", "2", "3", ] 
        
        result = '' 
        
        #call all methods
        for b in buttons :
            print "Button name=>"+b
            result += self.getMeaning(b)
        
        return result
    #eof getFullInterpretation
    

    def _getMeaning(self, sectionName):
        card = self.card
        # get any files into images directory
        curdir = dirname(__file__)
        filename = join(curdir, 'meanings', sectionName+".py")
        try:
            f = open(filename, "r") 
        except IOError:
            f = open(filename, "w+r") 
            text = (
'''#-*-coding:utf8;-*-

buf = " още няма данни, попълни %s" ''') % (sectionName, ) 
            f.write(text) 
            f.flush()
            f.seek(0)
            
        contents = f.read() 
        #print(contents)
        f.close()
        
        #http://lucumr.pocoo.org/2011/2/1/exec-in-python/
        exec(contents) 
        # buf is defined in the file 
        return buf 
    #eof getMeaning(filename)
    
    
#eof class


if __name__ == "__main__":
    cardReader = CardInterpreter( [0, 
    	2, 2, 1,
    	1, 1, 1,
    	1, 1, 2], "event")
    	
    print(cardReader.getFullInterpretation()) 
    print (cardReader._getMeaning("1")) 
    print ("Done") 