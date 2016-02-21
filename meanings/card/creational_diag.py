#-*-coding:utf8;-*-

buf = "" 

a = card[1] 
b = card[5]
c = card[9]
norm = 5

if a > 1 and b > 0 and c > 1:
    buf = "Диагоналът за Творческа личност е запълнен" 
    power = a + b + c
    buf += "\nСилата му е %d при норма от %d"%(power, norm) 
    
    
    