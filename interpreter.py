#-*-coding:utf8;-*-
from os.path import join, dirname

class CardInterpreter:

    def __init__(self, card):
        self.card = card
    #eof def
    
    
    def getFullInterpretation(self):
        pass
    
    #eof def getFullInterpretation
    
    @staticmethod
    def getMeaning(filename):
        # get any files into images directory
        curdir = dirname(__file__)
        filename = join(curdir, 'meanings', filename)
        try:  
            f = open(filename, "r") 
        except IOError:
            f = open(filename, "w+r") 
            f.write("buf = 'още няма данни, попълни "+filename+"' ") 
            f.flush()
            f.seek(0)
            
        contents = f.read() 
        #print(contents)
        f.close()
        
        #http://lucumr.pocoo.org/2011/2/1/exec-in-python/
        exec(contents) 
        # buf is defined in the file 
        return buf 
        
    #eof getMeaning(filename):
    
        
#eof class

if __name__ == "__main__":
    cardReader = CardInterpreter( [0, 
    	2, 2, 1,
    	1, 1, 1,
    	1, 1, 2] )
    	
    cardReader.getFullInterpretation()
    print (cardReader.getMeaning("test.txt")) 
    print ("Done") 