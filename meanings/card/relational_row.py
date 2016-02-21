#-*-coding:utf8;-*-

buf = "" 

a = card[2] 
b = card[5]
c = card[8]
norm = 4


if a > 1 and b > 0 and c > 0:
    buf = "редът за Взаимоотношения е запълнен" 
    power = a + b + c
    buf += "\nСилата му е %d при норма от %d"%(power, norm) 
   
   
    