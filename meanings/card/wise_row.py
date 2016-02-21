#-*-coding:utf8;-*-

buf = "" 

a = card[3] 
b = card[6]
c = card[9]
norm = 4


if a > 0 and b > 0 and c > 1:
    buf = "редът за Мъдрост е запълнен" 
    power = a + b + c
    buf += "\nСилата му е %d при норма от %d"%(power, norm) 
    

    