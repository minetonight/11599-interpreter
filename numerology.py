birthday = input("Enter full birthday e.g. ddmmyyyy") 
print(birthday+1) 
birthdayStr = str(birthday)

baseCard = [2,2,1,
1,1,1,
1,1,2] 


personalCard = [0] * 9
personalZeros = 0
personalDate = int(birthdayStr[0:2]) 
personalNumber = 0
personalNumberSimplified = 0

for num in birthdayStr:
    num = int(num)
    personalNumber += num
    
    if num == 0:
        personalZeros += 1
    else:
        personalCard[num-1] += 1

def addToCard(num):
    print('todo') 
    pass
        
addToCard(personalNumber) 

def simplifyNumber(num):
    print('todo') 
    pass

# def simplifyNumber
personalNumberSimplified = personalNumber
while personalNumberSimplified > 12:
    if personalNumberSimplified > 12:
        pNumStr = str(personalNumberSimplified) 
        personalNumberSimplified = int(pNumStr[0]) + 	int(pNumStr[1])
        addToCard(personalNumberSimplified)

def adjustPersonalNumber(num):
    year = int(birthdayStr[4:8]) 
    print(year)
    
    if year < 2000:
        addToCard(2)
        result = personalNumber - 2
        addToCard(result) 
        print (result) 
        simplifyNumber (result) 
    else:
        addToCard(19)
        result = personalNumber + 19
        addToCard(result) 
        print(result) 
        simplifyNumber (result) 
    
adjustPersonalNumber(personalNumber) 

print(baseCard) 
print(personalCard) 
print(personalDate) 
print(personalNumber) 
print(personalNumberSimplified) 


