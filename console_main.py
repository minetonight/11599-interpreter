from numerology import CardCalculator
from interpreter import CardInterpreter
from numbers import NumbersInterpreter

birthday = raw_input("Enter full birthday e.g. ddmmyyyy") 
print(birthday) 

baseCard = [2,2,1,
1,1,1,
1,1,2] 
# print(baseCard) 

calculator = CardCalculator(birthday)

#numReader = NumbersInterpreter() 
print(NumbersInterpreter.getDateInterpretation(calculator.personalDate)) 
print(NumbersInterpreter.getPersonalNumberInterpretation(calculator.personalNumberSimplified)) 

cardReader = CardInterpreter(calculator.personalCard)
cardReader.getFullInterpretation()

