#-*-coding:utf8;-*-

buf = "" 

a = card[3] 
b = card[5]
c = card[7]
norm = 3

if a > 0 and b > 0 and c > 0:
    buf = "Диагоналът за ?Чувствена? личност е запълнен" 
    power = a + b + c
    buf += "\nСилата му е %d при норма от %d"%(power, norm) 
    