class CardCalculator:
    
    def __init__(self, birthday):
        self.debug = True
        
        self.birthday = birthday
        self.personalCard = [0] * 10
        self.personalDate = int(str(birthday)[0:2]) 
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
            self.personalCard[num] += 1
        
    
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
        self.addToCard(result) 
        if self.debug:
            print(result) 
        self.simplifyNumber(result) 
    
    def formatProcess(self):
        
        print("%s = %s = %s") % (self.birthday, self.personalNumber, self.personalNumberSimplified) 
        print("%s & %s = %s == %s") % ( self.personalNumber, self.adjustment, 0, 0) 
        
        print(self.personalDate) 
        print(self.personalNumber) 
        print(self.personalNumberSimplified) 
        print(self.personalCard)
        
#eof class



birthday = 12121976 #input("Enter full birthday e.g. ddmmyyyy") 
print(birthday) 

baseCard = [2,2,1,
1,1,1,
1,1,2] 


calculator = CardCalculator(birthday)