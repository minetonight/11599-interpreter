#-*-coding:utf8;-*-
from os.path import join, dirname
from numerology import CardCalculator 

class CardInterpreter:
    
    personal_buttons = ["date_number", "personal_number"] 
    mid_card_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] 
    card_patterns_buttons = ["ego_or_altru", "sensitive_row", "relational_row", "wise_row", 
    'creational_diag', 'sensual_diag', 
    'self_col', 'others_col', 'higherself_col',  
    'bolt_and_nut'] 
    
    
    def __init__(self, cardCalculator, readingType):
        self.card = cardCalculator.card
        self.calc = cardCalculator 
        self.readingType = readingType
    #eof __init__
    
    
    def getMeaning(self, buttonName):
        folder = '' 
        filename = '' 
        
        # check buttons types 
        if buttonName == "date_number":
            filename = str(self.calc.personalDate)
            if self.readingType == "date":
                folder = 'date' 
            elif self.readingType == "year":
                folder = 'year'
            else:
                folder = 'birthday' 
            
        elif buttonName == "personal_number":
            filename = str(self.calc.personalNumberSimplified)
            if self.readingType == "date":
                folder = 'dateSum' 
            elif self.readingType == "year":
                folder = 'yearSum' 
            else:
                folder = 'personalSum'
            
        elif buttonName in self.mid_card_buttons:
            folder = 'card' 
            filename = buttonName + str(self.card[int(buttonName)] ) 
        
        elif buttonName in self.card_patterns_buttons:
            folder = 'card' 
            filename = buttonName
        
        return self._getMeaning(folder, filename)
    
    
    def getFullInterpretation(self):
        #print(dir(self)) 
        
        #get all methods of this class
        buttons = self.personal_buttons \
                + self.mid_card_buttons \
                + self.card_patterns_buttons \
        
        result = str(self.calc) +'\n' 
        
        #call all methods
        for b in buttons :
            print "Button name=>"+b
            result += self.getMeaning(b)
            result += "\n\n"
        
        return result
    #eof getFullInterpretation
    

    def _getMeaning(self, folder, fname):
        card = self.card
        # get any files into images directory
        curdir = dirname(__file__)
        filename = join(curdir, 'meanings', folder, fname+".py")
        try:
            f = open(filename, "r") 
        except IOError:
            f = open(filename, "w+r") 
            text = (
'''#-*-coding:utf8;-*-

buf = " още няма данни, попълни %s/%s" ''') % (folder, fname) 
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
    cardReader = CardInterpreter( CardCalculator("21111985") , "event")
    	
    #print(cardReader.getFullInterpretation()) 
    print (cardReader._getMeaning("personalSum", "12")) 
    print ("Done") 
    
    
    
    