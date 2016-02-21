#-*-coding:utf8;-*-

buf = "" 

if card[2] > 0 and card[5] > 0 and card[8] > 0:
    buf = "редът за Взаимоотношения е запълнен" 
    power = card[2] + card[5] + card[8]
    buf += "\nСилата му е %d при норма от %d"%(power, 3) 
    