from numerology import CardCalculator
from interpreter import CardInterpreter

birthday = 21111985 #input("Enter full birthday e.g. ddmmyyyy") 
print(birthday) 

baseCard = [2,2,1,
1,1,1,
1,1,2] 
print(baseCard) 

calculator = CardCalculator(birthday)

numReader = NumbersInterpreter() 
numReader.getDateInterpretation(calculator.personalDate)
numReader.getNumberInterpretation(calculator.personalNumberSimplified) )

cardReader = CardInterpreter(calculator.personalCard)
cardReader.getFullInterpretation()

