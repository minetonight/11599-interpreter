#-*-coding:utf8;-*-

buf = "" 

a = card[1] 
b = card[4]
c = card[7]
norm = 4

if a > 1 and b > 0 and c > 0:
    buf = "Редът за Сензитив е запълнен" 
    power = a + b + c
    buf += "\nСилата му е %d при норма от %d"%(power, norm) 
    
    
    
    