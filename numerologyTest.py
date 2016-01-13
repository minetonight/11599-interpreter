#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from numerology import CardCalculator
#from interpreter import CardInterpreter

def test(birthday, referenceCard): 
    calculator = CardCalculator(birthday)
    
    for i in range(len(referenceCard)):
        if calculator.personalCard[i] != referenceCard[i]:
            print (str(birthday) + " has unexpected result")  
            print ("reference card is" + str(referenceCard) ) 
            return False
            
    print("test passed") 
    return True


test(21111985, 
[1,
5, 4, 0,
0, 1, 1,
0, 3, 1]) 

