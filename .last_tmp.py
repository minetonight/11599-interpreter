class CardCalculator:
    
    def __init__(self, birthday):
        self.debug = True
        
        self.birthday = birthday
        self.personalCard = [0] * 10
        self.personalDate = int(str(birthday)[0:2]) 
        self.personalNumber = 0
        self.personalNumberSimplified = 0
        
        self.addToCard(birthday, True)
        self.adjustPersonalNumber(self.personalNumber) 
        self.personalNumberSimplified = self.simplifyNumber(self.personalNumber)
        
        self.addToCard(self.personalNumber)
        
        print(self.personalDate) 
        print(self.personalNumber) 
        print(self.personalNumberSimplified) 
        print(self.personalCard) 

    
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
        print(year)
        
        if year < 2000:
            self.addToCard(2)
            result = self.personalNumber - 2
            self.addToCard(result) 
            print (result) 
            self.simplifyNumber(result) 
        else:
            self.addToCard(19)
            result = self.personalNumber + 19
            self.addToCard(result) 
            print(result) 
            self.simplifyNumber(result) 
        
#eof class



birthday = 12121978 #input("Enter full birthday e.g. ddmmyyyy") 
print(birthday) 

baseCard = [2,2,1,
1,1,1,
1,1,2] 


calculator = CardCalculator(birthday)