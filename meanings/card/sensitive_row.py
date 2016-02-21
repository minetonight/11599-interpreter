#-*-coding:utf8;-*-

buf = "" 

if card[1] > 1 and card[4] > 0 and card[7] > 0:
    buf = "Редът за Сензитив е запълнен" 
    power = card[1] + card[4] + card[7]
    buf += "\nСилата му е %d при норма от %d"%(power, 4) 
    
    
    
    