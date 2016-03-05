#-*-coding:utf8;-*-

buf = "" 

a = card[7] 
b = card[8]
c = card[9]
norm = 4


if a > 0 and b > 0 and c > 1:
    buf = "Колоната за вътрешен свят е запълнена" 
    power = a + b + c
    buf += "\nСилата ѝ е %d при норма от %d"%(power, norm) 
   
   
    