class CardCalculator:
    
    def __init__(self, birthday):
        #self.debug = True
        self.debug = False
        
        self.birthday = birthday
        self.card = [0] * 10
        self.personalDate = int(birthday[0:2]) 
        self.personalNumber = 0
        self.personalNumberSimplified = 0
        self.adjustment = 0
        
        self.addToCard(birthday, True)
        self.personalNumberSimplified = self.simplifyNumber(self.personalNumber)
        self.adjustPersonalNumber(self.personalNumber) 
        
        self.addToCard(self.personalNumber)
        
        self.formatProcess() 

    
    def addToCard(self, number, addToPersonal=False):
        strNum = str(number)
        
        for num in strNum:
            num = int(num)
            self.card[num] += 1
        
    
            if self.debug:
                print("add to card " + str(num)) 
        
            if addToPersonal:
                self.personalNumber += num
            
    def simplifyNumber(self, number):
        while number > 12:
            
            if self.debug:
                print("simplify " + str(number) ) 
            
            if number > 12:
                pNumStr = str(number) 
                number = int(pNumStr[0]) + 	int(pNumStr[1])
                self.addToCard(number)
        
        
        return number

    def adjustPersonalNumber(self, num):
        year = int(str(self.birthday)[4:8]) 
        
        if self.debug:
            print(year)
        
        if year < 2000:
            self.adjustment = -2
        else:
            self.adjustment = 19
            
            
        self.addToCard(abs(self.adjustment))
        result = self.personalNumber + self.adjustment 
        self.adjusted = result
        
        self.addToCard(result) 
        if self.debug:
            print(result) 
        self.adjustedSimple = self.simplifyNumber(result) 
    
    def formatProcess(self):
        
        print("%s = %s = %s") % (self.birthday, self.personalNumber, self.personalNumberSimplified) 
        print("%s & %s = %s == %s") % ( self.personalNumber, self.adjustment, self.adjusted, self.adjustedSimple) 
        
        print(self.personalDate) 
        #print(self.personalNumber) 
        #print(self.personalNumberSimplified) 
        print(self.card)
        
        
    def __str__(calc):
        text = \
"""
birthday = %s
personalNumber = %s
      |      |      
%6s|%6s|%6s
      |      |      
---------------------
      |      |      
%6s|%6s|%6s
      |      |      
---------------------
      |      |      
%6s|%6s|%6s
      |      |      
---------------------
      |      |      
      |%6s|      
      |      |      
"""
        	
        text = text % (calc.birthday, 
        calc.personalNumberSimplified, 
        "1" * calc.card[1], "4" * calc.card[4], "7" * calc.card[7], 
        "2" * calc.card[2], "5" * calc.card[5], "8" * calc.card[8], 
        "3" * calc.card[3], "6" * calc.card[6], "9" * calc.card[9], 
        "0" * calc.card[0]) 
        return text
        
#eof class

if __name__ == "__main__":

    birthday = "21111985" #input("Enter full birthday e.g. ddmmyyyy") 
    print(birthday) 
    
    calculator = CardCalculator(birthday)
    print str(calculator) 




