@deprecated 
class NumbersInterpreter:
    
    def __init__(self):
        pass
    #eof def
    
    @staticmethod
    def getDateInterpretation(date):
        
        if date == 1:
            return "1 is " 
        if date == 2:
            return "2 is " 
        if date == 3:
            return "3 is " 
        if date == 4:
            return "4 is " 
        if date == 5:
            return "5 is " 
        if date == 6:
            return "6 is " 
        if date == 7:
            return "7 is " 
        if date == 8:
            return "8 is " 
        if date == 9:
            return "9 is " 
        if date == 10:
            return "10 is " 
        if date == 11:
            return "11 is " 
        if date == 12:
            return "12 is " 
        if date == 13:
            return "13 is " 
        if date == 14:
            return "14 is " 
        if date == 15:
            return "15 is " 
        if date == 16:
            return "16 is " 
        if date == 17:
            return "17 is " 
        if date == 18:
            return "18 is " 
        if date == 19:
            return "19 is " 
        if date == 20:
            return "20 is " 
        if date == 21:
            return "21 is " 
        if date == 22:
            return "22 is " 
        if date == 23:
            return "23 is " 
        if date == 24:
            return "24 is " 
        if date == 25:
            return "25 is " 
        if date == 26:
            return "26 is " 
        if date == 27:
            return "27 is " 
        if date == 28:
            return "28 is " 
        if date == 29:
            return "29 is " 
        if date == 30:
            return "30 is " 
        if date == 31:
            return "31 is "
    #eof 
    
    
    @staticmethod
    def getPersonalNumberInterpretation(number):
        if number == 1:
            return "1 is " 
        if number == 2:
            return "2 is " 
        if number == 3:
            return "3 is " 
        if number == 4:
            return "4 is " 
        if number == 5:
            return "5 is " 
        if number == 6:
            return "6 is " 
        if number == 7:
            return "7 is " 
        if number == 8:
            return "8 is " 
        if number == 9:
            return "9 is " 
        if number == 10:
            return "10 is " 
        if number == 11:
            return "11 is " 
        if number == 12:
            return "12 is " 
    #eof 
    
#eof class

if __name__ == "__main__":
    numReader = NumbersInterpreter() 
    numReader.getDateInterpretation(calculator.personalDate)
    numReader.getNumberInterpretation(calculator.personalNumberSimplified)
