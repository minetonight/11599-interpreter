#-*-coding:utf8;-*-

buf = "" 

a = card[1] 
b = card[2]
c = card[3]
norm = 5


if a > 1 and b > 1 and c > 0:
    buf = "Колоната за самостоятелност е запълнена" 
    power = a + b + c
    buf += "\nСилата ѝ е %d при норма от %d"%(power, norm) 
   
   
    